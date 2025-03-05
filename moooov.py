

class ProcessMoovQRView(View):
    def get(self, request):
        agent_number = request.GET.get('agent_number', '')
        
        if not agent_number:
            return redirect('client:scan')
            
        form = MoovClientForm()
        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None  # On initialise sans code
        })
    
    def post(self, request):
        agent_number = request.GET.get('agent_number', '')
        form = MoovClientForm(request.POST)
        
        if form.is_valid():
            secret_code = form.cleaned_data['secret_code']
            
            # Construction du code de transaction
            transaction_code = f"*155*5*1*{secret_code}#"
            
            # On renvoie directement le code pour qu'il s'affiche sur la page
            return render(request, 'client/moov_form.html', {
                'form': form,
                'agent_number': agent_number,
                'transaction_code': transaction_code  # On passe le code à la page
            })
        
        return render(request, 'client/moov_form.html', {
            'form': form,
            'agent_number': agent_number,
            'transaction_code': None
        })