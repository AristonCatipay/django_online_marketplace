from django import forms
from . models import Item

INPUT_CLASSES = 'rounded-none rounded-e-lg bg-gray-50 border border-gray-300 text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
CHECKBOX = 'w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': SELECT_AREA,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder' : "Enter name",
            }),
            'description': forms.Textarea(attrs={
                'class': TEXT_AREA,
                'placeholder' : "Enter description..",
                'rows' : '4',
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder' : "Enter price",
            }),
            'image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': TEXT_AREA,
                'placeholder' : "Enter description..",
                'rows' : '4',
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder' : "Enter price",
            }),
            'image': forms.FileInput(attrs={
                'class': FOR_IMAGE,
            }),
            'is_sold': forms.CheckboxInput(attrs={
                'class': CHECKBOX,
            }),
        }        