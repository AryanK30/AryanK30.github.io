<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gross_salary = float(request.form.get('grossSalary', 0))
        nis_rate = 5.6
        first_income_tax_rate = 25
        second_income_tax_rate = 35
        first_threshold = 130000
        second_threshold = 260000
        deductions = 0

        if gross_salary <=first_threshold:

          # Calculate NIS contribution
          nis_contribution = gross_salary * (nis_rate / 100)
        
          #Calculate Net Salary
          net_salary = gross_salary - nis_contribution

          return jsonify({
              "NISpaid": round(nis_contribution, 2),
              "IncomeTaxPaid": round(income_tax, 2),
              "NetSalary": round(net_salary, 2)
        })
        

        elif gross_salary > first_threshold:

          # Calculate NIS contribution
          nis_contribution = gross_salary * (nis_rate / 100)

          # Taxable salary after NIS
          taxable_salary = gross_salary - nis_contribution - first_threshold
          taxable_salary = max(taxable_salary, 0)  # Ensure it doesn't go negative

          # Calculate Income Tax
          if taxable_salary > second_threshold:
            first_income_tax = second_threshold * (first_income_tax_rate / 100)
            excess_income = taxable_salary - second_threshold
            second_income_tax = excess_income * (second_income_tax_rate / 100)
            income_tax = first_income_tax + second_income_tax
          else:
            income_tax = taxable_salary * (first_income_tax_rate / 100) 
          

          # Calculate Net Salary
          net_salary = gross_salary - nis_contribution - income_tax

          return jsonify({
              "NISpaid": round(nis_contribution, 2),
              "IncomeTaxPaid": round(income_tax, 2),
              "NetSalary": round(net_salary, 2)

        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


=======
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gross_salary = float(request.form.get('grossSalary', 0))
        nis_rate = 5.6
        first_income_tax_rate = 25
        second_income_tax_rate = 35
        first_threshold = 130000
        second_threshold = 260000
        deductions = 0

        if gross_salary <=first_threshold:

          # Calculate NIS contribution
          nis_contribution = gross_salary * (nis_rate / 100)
        
          #Calculate Net Salary
          net_salary = gross_salary - nis_contribution

          return jsonify({
              "NISpaid": round(nis_contribution, 2),
              "IncomeTaxPaid": round(income_tax, 2),
              "NetSalary": round(net_salary, 2)
        })
        

        elif gross_salary > first_threshold:

          # Calculate NIS contribution
          nis_contribution = gross_salary * (nis_rate / 100)

          # Taxable salary after NIS
          taxable_salary = gross_salary - nis_contribution - first_threshold
          taxable_salary = max(taxable_salary, 0)  # Ensure it doesn't go negative

          # Calculate Income Tax
          if taxable_salary > second_threshold:
            first_income_tax = second_threshold * (first_income_tax_rate / 100)
            excess_income = taxable_salary - second_threshold
            second_income_tax = excess_income * (second_income_tax_rate / 100)
            income_tax = first_income_tax + second_income_tax
          else:
            income_tax = taxable_salary * (first_income_tax_rate / 100) 
          

          # Calculate Net Salary
          net_salary = gross_salary - nis_contribution - income_tax

          return jsonify({
              "NISpaid": round(nis_contribution, 2),
              "IncomeTaxPaid": round(income_tax, 2),
              "NetSalary": round(net_salary, 2)

        })
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


>>>>>>> 340ddb1 (Initial commit)
