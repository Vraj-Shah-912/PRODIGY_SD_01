# converter/views.py
from django.shortcuts import render
from django.views import View
from .utils import convert_temperature

class ConverterView(View):
    def get(self, request):
        return render(request, 'converter/converter.html')

    def post(self, request):
        try:
            value = float(request.POST.get('value', 0))  # Default to 0 if value is not provided
            from_unit = request.POST.get('unit')

            if not value or not from_unit:
                raise ValueError("Please enter a temperature value and select a unit.")

            # Perform conversions
            results = {}
            if from_unit == 'C':
                results['Fahrenheit'] = convert_temperature(value, 'C', 'F')
                results['Kelvin'] = convert_temperature(value, 'C', 'K')
            elif from_unit == 'F':
                results['Celsius'] = convert_temperature(value, 'F', 'C')
                results['Kelvin'] = convert_temperature(value, 'F', 'K')
            elif from_unit == 'K':
                results['Celsius'] = convert_temperature(value, 'K', 'C')
                results['Fahrenheit'] = convert_temperature(value, 'K', 'F')

            return render(request, 'converter/converter.html', {
                'value': value,
                'from_unit': from_unit,
                'results': results,
            })
        except ValueError as e:
            error_message = str(e)
            return render(request, 'converter/converter.html', {'error_message': error_message})
