from django.shortcuts import render, redirect
from barang.models import *

# Create your views here.
def barang_list(request):
    template_name = 'barang_list.html'
    item_list = item.objects.all()
    context = {
        'title':'Item List',
        'item' : item_list
    }
    return render(request,template_name,context)

def barang_add(request):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all()
    if request.method == "POST":

        input_Kategori = request.POST.get('kategori')
        input_Nama = request.POST.get('Nama')
        input_jumlah = request.POST.get('jumlah')
        input_Deskripsi = request.POST.get('Deskripsi')

        get_kategori = Kategori.objects.get(nama=input_Kategori)

        item.objects.create(
            nama=input_Nama,
            jumlah = input_jumlah,
            Deskripsi = input_Deskripsi,
            kategori = get_kategori,
        )
        return redirect(barang_list)

        print(input_Kategori, input_Nama, input_jumlah, input_System_Deskripsi)
    context = {
        'title':'Add Barang',
        'kategori': kategori
    }
    return render(request,template_name,context)

def barang_update(request, id):
    template_name = 'barang_add.html'
    kategori = Kategori.objects.all()
    get_item = item.objects.get(id=id)
    if request.method == "POST":

        input_Kategori = request.POST.get('kategori')
        input_Nama = request.POST.get('Nama')
        input_jumlah = request.POST.get('jumlah')
        input_Deskripsi = request.POST.get('Deskripsi')

        get_kategori = Kategori.objects.get(nama=input_Kategori)

        get_item.nama = input_Nama
        get_item.jumlah = input_jumlah
        get_item.Deskripsi = input_Deskripsi
        get_item.Kategori = get_kategori
        get_item.save()
    
        return redirect(barang_list)

    context = {
        'title':'Add Barang',
        'kategori': kategori,
        'get_item':get_item,
    }
    return render(request,template_name,context)
    

def barang_delete(request, id):
    item = item.objects.get(id=id).delete()
    return redirect(barang_list)