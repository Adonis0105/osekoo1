from django.shortcuts import render, redirect
from django.views import View
from .forms import MoovClientForm

class ProcessMoovQRView(View):
    def get(self, request):
        agent_number = request.GET.get('agent_number', '')
        if not agent_number:
            return redirect('client:scan')

        form = MoovClientForm()
        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number
        })

    def post(self, request):
        agent_number = request.GET.get('agent_number', '')
        form = MoovClientForm(request.POST)

        if form.is_valid():
            secret_code = form.cleaned_data['secret_code']

            # Génération immédiate du code USSD pour Moov Money Flooz
            transaction_code = f"*155*5*1*{secret_code}#"

            # Rediriger immédiatement vers le clavier téléphonique
            return redirect(f"tel:{transaction_code}")

        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number
        })
