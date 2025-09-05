from odoo import models

class PetReport(models.AbstractModel):
    _name= 'report.pet_care_management_shine.pet_report'
    _inherit = 'report.report_xlsx.abstract'
    _description= "Abstract XLSX Report For Pet"
    
    
    
    def generate_xlsx_report(self, workbook, data, pets):
        sheet = workbook.add_worksheet("Pet Report")

        # Formatting Styles
        title_format = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter'})
        header_format = workbook.add_format({'bold': True, 'bg_color': '#4472C4', 'font_color': 'white', 'align': 'center', 'border': 1})
        date_format = workbook.add_format({'num_format': 'yyyy-mm-dd', 'align': 'center', 'border': 1})
        text_format = workbook.add_format({'align': 'left', 'border': 1})
        center_format = workbook.add_format({'align': 'center', 'border': 1})
        alt_row_format = workbook.add_format({'bg_color': '#DDEBF7', 'border': 1})

        # Set column widths
        sheet.set_column(0, 0, 15)  # Pet ID
        sheet.set_column(1, 1, 25)  # Pet Name
        sheet.set_column(2, 2, 15)  # Species
        sheet.set_column(3, 3, 10)  # Gender
        sheet.set_column(4, 4, 25)  # Breed
        sheet.set_column(5, 5, 15)  # Date of Birth
        sheet.set_column(6, 6, 10)  # Age
        sheet.set_column(7, 7, 25)  # Owner
        sheet.set_column(8, 8, 40)  # Services

        # Title
        sheet.merge_range('A1:I1', "Pet Details Report", title_format)

        # Headers
        headers = ["Pet ID", "Name", "Species", "Gender", "Breed", "DOB", "Age", "Owner", "Services"]
        for col, header in enumerate(headers):
            sheet.write(2, col, header, header_format)

        # Data Rows
        row = 3
        for pet in pets:
            format_to_use = alt_row_format if row % 2 == 1 else text_format

            sheet.write(row, 0, pet.sequence_number, center_format)
            sheet.write(row, 1, pet.name, format_to_use)
            sheet.write(row, 2, dict(pet._fields['species'].selection).get(pet.species), center_format)
            sheet.write(row, 3, dict(pet._fields['gender'].selection).get(pet.gender), center_format)
            sheet.write(row, 4, pet.breed, format_to_use)
            sheet.write_datetime(row, 5, pet.date_of_birth, date_format)
            sheet.write(row, 6, pet.age, center_format)
            sheet.write(row, 7, pet.owner_id.name if pet.owner_id else "", format_to_use)

            # Join service names into a comma-separated string
            services = ", ".join(pet.service_ids.mapped('name'))
            sheet.write(row, 8, services, format_to_use)

            row += 1