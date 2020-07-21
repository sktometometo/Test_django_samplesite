from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.views.decorators.http import require_http_methods

from .models import Part, Transaction
from .forms import PartForm, TransactionForm

# Create your views here.

def updateAmount():
    parts = Part.objects.all()
    for part in parts:
        transactions = Transaction.objects.filter(transaction_part=part)
        result = 0
        for tr in transactions:
            result += tr.transaction_diff
        part.part_amount = result
        part.save()

@require_http_methods(['GET'])
def part_index(request):
    list_parts = Part.objects.all()
    return render(
            request,
            'partlist/part_index.html',
            {'list_parts': list_parts}
            )

@require_http_methods(['GET','POST'])
def part_add(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.part_amount = 0
            part.save()
            return redirect('part_detail', pk=part.pk)
        return render(
                request,
                'partlist/part_edit.html',
                {'form': form,
                 'is_error': True}
                )
    else:
        form = PartForm()
        return render(
                request,
                'partlist/part_edit.html',
                {'form': form,
                 'is_error': False}
                )

@require_http_methods(['POST'])
def part_delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        delete_ids = map( int, delete_ids )
        for did in delete_ids:
            Transaction.objects.filter(transaction_part=did).delete()
            Part.objects.filter(pk=did).delete()
    updateAmount()
    return redirect('part_index')

@require_http_methods(['GET','POST'])
def part_edit(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
        if form.is_valid():
            part = form.save()
            part.save()
            return redirect('part_detail', pk=part.pk)
        else:
            return render(
                    request,
                    'partlist/part_edit.html',
                    {'form': form,
                     'is_error': True}
                    )
    else:
        form = PartForm(instance=part)
        return render(
                request,
                'partlist/part_edit.html',
                {'form': form,
                 'is_error': False}
                )

@require_http_methods(['GET'])
def part_detail(request, pk):
    part = get_object_or_404(Part, pk=pk)
    list_transactions = Transaction.objects.filter(transaction_part=part).order_by('-transaction_date')
    return render(
            request,
            'partlist/part_detail.html',
            {'part': part,
             'list_transactions': list_transactions}
            )



@require_http_methods(['GET'])
def transaction_index(request):
    list_transactions = Transaction.objects.order_by('-transaction_date')
    template = loader.get_template('partlist/transaction_index.html')
    context = {
        'list_transactions': list_transactions,
    }
    return HttpResponse(template.render(context, request))

@require_http_methods(['GET','POST'])
def transaction_add(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            # transaction.transaction_user = request.user
            transaction.save()
            updateAmount()
            return redirect('transaction_index')
        return render(
                request,
                'partlist/transaction_edit.html',
                {'form': form,
                 'is_error': True}
                )
    else:
        form = TransactionForm()
        return render(
                request,
                'partlist/transaction_edit.html',
                {'form': form,
                 'is_error': False}
                )

@require_http_methods(['POST'])
def transaction_delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        delete_ids = map( int, delete_ids )
        for did in delete_ids:
            Transaction.objects.filter(pk=did).delete()
    updateAmount()
    return redirect('transaction_index')

@require_http_methods(['GET','POST'])
def transaction_edit(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.save()
            updateAmount()
            return redirect('transaction_index')
        else:
            return render(
                    request,
                    'partlist/transaction_edit.html',
                    {'form': form,
                     'is_error': True}
                    )
    else:
        form = TransactionForm(instance=transaction)
        return render(
                request,
                'partlist/transaction_edit.html',
                {'form': form,
                 'is_error': False}
                )
