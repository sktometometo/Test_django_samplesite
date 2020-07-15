from django import forms

from .models import Part, Transaction

class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ('part_name',
                  'part_number',
#                  'part_amount',
                  'part_unit',
                  'part_place',
                  'part_supplier',
                  'part_remark',
                  )


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ('transaction_date',
                  'transaction_part',
                  'transaction_diff',
                  'transaction_remark',
                  )
