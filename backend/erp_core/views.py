from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import importlib

@csrf_exempt
def frappe_rpc(request):
    """
    Simulates Frappe's RPC mechanism.
    Expects POST with 'method' in params and JSON data.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            method_path = request.GET.get('method') or data.get('method')

            # Simplified resolution logic: module.path.function
            parts = method_path.split('.')
            module_name = '.'.join(parts[:-1])
            func_name = parts[-1]

            # Attempt to import and call
            # This is a placeholder for actual business logic handlers
            return JsonResponse({'message': f'Method {method_path} called', 'status': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)
