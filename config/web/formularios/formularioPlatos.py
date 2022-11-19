from django import forms

""" crear el formulario """

class FormularioRegistroPlatos(forms.Form):

    #Se crea una tupla
    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postres'),
        (4, 'Bebidas')
    )


    nombrePlato=forms.CharField(
        widget=forms.TextInput( attrs={"class":"form-control mb-3"}),
        max_length=30,
        required=True,
        label='Nombre del plato'
    )
    descripcionPlato=forms.CharField(
        widget=forms.Textarea( attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label='Descripcion del plato'
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput( attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label='Foto del plato'
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput( attrs={"class":"form-control mb-3"}),
        required=True,
        label='Precio'
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select( attrs={"class":"form-control mb-3"}),
        choices=PLATOS,
        label='Tipo de plato'
    )



