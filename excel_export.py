from openpyxl import Workbook
from io import BytesIO


def create_excel(results):
    """
    Creates an Excel file from candidate results.
    """

    wb = Workbook()
    ws = wb.active

    ws.title = "Resume Analysis"

    # Header
    ws.append([
        "Candidate",
        "Match Score",
        "Recommendation"
    ])

    # Data
    for candidate in results:

        ws.append([
            candidate["name"],
            candidate["score"],
            candidate["recommendation"]
        ])

    output = BytesIO()

    wb.save(output)

    output.seek(0)

    return output