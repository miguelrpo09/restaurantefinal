from django import forms


class FormularioEmpleados(forms.Form):

    #idEmpleado
    #nombreEmpleado
    #apellidoEmpleado
    #cargoEmpleado
    #direccionEmpleado
    #salarioMensualEmpleado


    idEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Identificación'
    )
    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Nombre Empleado'
    )
    apellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Apellido Empleado'
    )
    cargoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Cargo Empleado'
    )
    direccionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Dirección Empleado'
    )
    salarioMensualEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3'}),
        max_length=30,
        required=True,
        label='Salario Mensual Empleado'
    )


    