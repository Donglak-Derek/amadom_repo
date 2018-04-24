from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "amadon/index.html")

def process(request):
	print request.POST
	if request.method == "POST":

		request.session['price'] = request.POST['price']

		quantity = int(request.POST['quantity']) 

		if "quantity" not in request.session:
			request.session['quantity'] = quantity

		else:
			request.session['quantity'] += quantity

		Sum = float(request.POST['price']) * int(request.POST['quantity'])

		if "total" not in request.session:

			request.session['total'] = 0
		request.session['total'] += Sum    #total = total + sum

	return redirect("/amadon/checkout")

def checkout(request):
	return render(request, "amadon/checkout.html")

def logout(request):

	request.session.flush()

	# del request.session['quantity']
	# del request.session['total']
	return redirect("/amadon")