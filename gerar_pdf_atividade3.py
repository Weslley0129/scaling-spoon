from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


BASE = Path(__file__).resolve().parent
OUT = BASE / "atividade3-entrega.pdf"


def read_text(name: str) -> str:
    path = BASE / name
    if not path.exists():
        return f"[Arquivo nao encontrado: {name}]"
    return path.read_text(encoding="utf-8")


def lines_from_markdown(raw: str) -> list[str]:
    lines = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            lines.append("")
            continue
        if line.startswith("```"):
            continue
        if line.startswith("#"):
            line = line.lstrip("#").strip()
            line = line.upper()
        if line.startswith("- "):
            line = f"• {line[2:]}"
        lines.append(line)
    return lines


def build():
    styles = getSampleStyleSheet()
    normal = ParagraphStyle(
        "NormalCustom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        spaceAfter=4,
    )
    title = ParagraphStyle(
        "TitleCustom",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        spaceAfter=12,
    )

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
        title="Atividade 3 - Entrega",
        author="Aluno(a)",
    )

    story = [Paragraph("Atividade 3 - Transformacao SQL para NoSQL", title)]

    sections = [
        ("DER", read_text("atividade3-der.md")),
        ("Codigo SQL", read_text("atividade3-modelagem.sql")),
        ("Codigo MongoDB", read_text("atividade3-mongodb.js")),
        ("Kanban e Papéis Scrum", read_text("atividade3-kanban-scrum.md")),
    ]

    for section_name, content in sections:
        story.append(Spacer(1, 8))
        story.append(Paragraph(section_name, ParagraphStyle("H2", parent=normal, fontName="Helvetica-Bold", fontSize=12)))
        story.append(Spacer(1, 6))
        for line in lines_from_markdown(content):
            safe = (
                line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
            )
            if safe == "":
                story.append(Spacer(1, 4))
            else:
                story.append(Paragraph(safe, normal))

    doc.build(story)


if __name__ == "__main__":
    build()
