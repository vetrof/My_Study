# shirtificate
# add name to image and save him in pdf file
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/psets/8
# Vitaly (Vetrof) / vetrof@gmail.com  / vetrof.com


from fpdf import FPDF, drawing


class PDF(FPDF):

    def header(self):
        # print header
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 35)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        # self.cell(0)
        self.ln(20)

    def tshirt(self):
        # Print tshirt
        # self.image('shirtificate.png', w=183)
        self.image('shirtificate.png', w=self.epw)

    def print_name(self, name):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 25)

        self.text_color = drawing.DeviceGray(255 / 255)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, -250, name, border=0, align="C")
        # self.cell(100, 100, "CS50 Shirtificate", border=1, align="C")
        # Performing a line break:
        self.ln(20)


def main():
    name = input('Name: ')

    pdf = PDF()
    pdf.add_page()
    pdf.tshirt()
    pdf.print_name(name)
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()
