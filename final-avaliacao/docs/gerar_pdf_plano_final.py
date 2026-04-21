from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

base = Path(__file__).resolve().parent
md = base / "plano-de-testes-web.md"
pdf = base / "plano-de-testes-web.pdf"

text = md.read_text(encoding="utf-8")
styles = getSampleStyleSheet()
normal = ParagraphStyle("N", parent=styles["Normal"], fontSize=10, leading=14)
title = ParagraphStyle("T", parent=styles["Title"], fontSize=16, leading=20)

doc = SimpleDocTemplate(str(pdf), pagesize=A4, leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)
story = [Paragraph("Plano de Testes Web - Entrega Final", title), Spacer(1, 8)]

for line in text.splitlines():
    line = line.strip()
    if not line:
        story.append(Spacer(1, 4))
        continue
    if line.startswith("#"):
        line = line.lstrip("#").strip().upper()
    if line.startswith("- "):
        line = "• " + line[2:]
    safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    story.append(Paragraph(safe, normal))

doc.build(story)
print(f"PDF gerado: {pdf}")
