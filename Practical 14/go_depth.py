from __future__ import annotations
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
from xml.dom import minidom
import xml.sax
TARGET_NAMESPACES = [
    "molecular_function",
    "biological_process",
    "cellular_component",
]
@dataclass
class GOTermRecord:
    #Stores the best GO term found for a namespace."""
    go_id: str = ""
    name: str = ""
    namespace: str = ""
    is_a_count: int = -1
def child_text_dom(parent, tag_name: str) -> str:
    #Return text inside the first child element called tag_name."""
    children = parent.getElementsByTagName(tag_name)
    if not children:
        return ""
    pieces = []
    for node in children[0].childNodes:
        if node.nodeType == node.TEXT_NODE:
            pieces.append(node.data)
    return "".join(pieces).strip()
def update_best(best: Dict[str, GOTermRecord], go_id: str, name: str, namespace: str, is_a_count: int) -> None:
    #Update the best term for a namespace if this term has more <is_a> elements.
    if namespace not in TARGET_NAMESPACES:
        return
    if is_a_count > best[namespace].is_a_count:
        best[namespace] = GOTermRecord(go_id, name, namespace, is_a_count)
def analyse_with_dom(xml_file: Path) -> tuple[Dict[str, GOTermRecord], float]:
    #Analyse the XML file using DOM/minidom."""
    start = datetime.now()
    document = minidom.parse(str(xml_file))
    terms = document.getElementsByTagName("term")
    best = {namespace: GOTermRecord(namespace=namespace) for namespace in TARGET_NAMESPACES}
    for term in terms:
        go_id = child_text_dom(term, "id")
        name = child_text_dom(term, "name")
        namespace = child_text_dom(term, "namespace")
        is_a_count = len(term.getElementsByTagName("is_a"))
        update_best(best, go_id, name, namespace, is_a_count)
    elapsed = (datetime.now() - start).total_seconds()
    return best, elapsed
class GOHandler(xml.sax.ContentHandler):
    #SAX handler for finding GO terms with the highest <is_a> counts."""
    def __init__(self) -> None:
        super().__init__()
        self.current_tag = ""
        self.inside_term = False
        self.go_id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0
        self.best = {namespace: GOTermRecord(namespace=namespace) for namespace in TARGET_NAMESPACES}
    def startElement(self, tag, attrs):  # noqa: N802 - SAX requires this name
        self.current_tag = tag
        if tag == "term":
            self.inside_term = True
            self.go_id = ""
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0
        elif self.inside_term and tag == "is_a":
            self.is_a_count += 1
    def characters(self, content):
        if not self.inside_term:
            return
        # SAX may split character data into several chunks, so use +=.
        if self.current_tag == "id":
            self.go_id += content
        elif self.current_tag == "name":
            self.name += content
        elif self.current_tag == "namespace":
            self.namespace += content
    def endElement(self, tag):  # noqa: N802 - SAX requires this name
        if tag == "term":
            update_best(
                self.best,
                self.go_id.strip(),
                self.name.strip(),
                self.namespace.strip(),
                self.is_a_count,
            )
            self.inside_term = False
        self.current_tag = ""
def analyse_with_sax(xml_file: Path) -> tuple[Dict[str, GOTermRecord], float]:
    #Analyse the XML file using SAX.
    start = datetime.now()
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = GOHandler()
    parser.setContentHandler(handler)
    parser.parse(str(xml_file))
    elapsed = (datetime.now() - start).total_seconds()
    return handler.best, elapsed
def print_results(method_name: str, results: Dict[str, GOTermRecord], elapsed: float) -> None:
    #Print results in a clear portfolio-friendly format.
    print(f"\n{method_name} results")
    print("-" * 70)
    for namespace in TARGET_NAMESPACES:
        record = results[namespace]
        print(f"Ontology: {namespace}")
        print(f"  GO ID: {record.go_id}")
        print(f"  Term name: {record.name}")
        print(f"  Number of <is_a> elements: {record.is_a_count}")
    print(f"Time taken by {method_name}: {elapsed:.6f} seconds")
def compare_results(dom_results: Dict[str, GOTermRecord], sax_results: Dict[str, GOTermRecord]) -> None:
    """Check whether DOM and SAX gave the same best terms/counts."""
    same = True
    for namespace in TARGET_NAMESPACES:
        d = dom_results[namespace]
        s = sax_results[namespace]
        if (d.go_id, d.name, d.is_a_count) != (s.go_id, s.name, s.is_a_count):
            same = False
            print(f"WARNING: DOM and SAX differ for {namespace}")
    if same:
        print("\nDOM and SAX returned the same results.")

def main() -> None:
    if len(sys.argv) > 1:
        xml_file = Path(sys.argv[1])
    else:
        xml_file = Path("go_obo.xml")
        if not xml_file.exists() and Path("go_obo_sample.xml").exists():
            print("go_obo.xml not found, so using go_obo_sample.xml for demonstration.")
            xml_file = Path("go_obo_sample.xml")

    if not xml_file.exists():
        raise FileNotFoundError(
            "Could not find the XML input file. Put go_obo.xml in this folder "
            "or run: python go_depth.py path/to/go_obo.xml"
        )
    print(f"Input XML file: {xml_file}")
    dom_results, dom_time = analyse_with_dom(xml_file)
    sax_results, sax_time = analyse_with_sax(xml_file)

    print_results("DOM", dom_results, dom_time)
    print_results("SAX", sax_results, sax_time)
    compare_results(dom_results, sax_results)

    if sax_time < dom_time:
        print(f"\nFastest API: SAX ({sax_time:.6f} seconds)")
    elif dom_time < sax_time:
        print(f"\nFastest API: DOM ({dom_time:.6f} seconds)")
    else:
        print("\nFastest API: DOM and SAX took the same time.")
if __name__ == "__main__":
    main()