from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import importlib
import inspect

# Whitelist of apps allowed for RPC
ALLOWED_APPS = [
    'accounts', 'assets', 'bulk_transaction', 'buying', 'communication',
    'controllers', 'crm', 'desktop_icon', 'domains', 'edi', 'erpnext_integrations',
    'maintenance', 'manufacturing', 'portal', 'projects', 'quality_management',
    'regional', 'report_center', 'selling', 'setup', 'shopping_cart', 'stock',
    'support', 'telephony', 'utilities', 'erp_core'
]

@csrf_exempt
def frappe_rpc(request):
    """
    Simulates Frappe's RPC mechanism with improved security and multi-prefix handling.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            method_path = request.GET.get('method') or data.get('method')

            if not method_path:
                return JsonResponse({'error': 'No method provided'}, status=400)

            parts = method_path.split('.')
            if len(parts) < 2:
                return JsonResponse({'error': 'Invalid method format'}, status=400)

            # Handle erpnext.app.func or frappe.func
            if parts[0] == 'erpnext':
                if len(parts) < 3:
                    return JsonResponse({'error': 'Invalid erpnext method format'}, status=400)
                app_label = parts[1]
                func_name = parts[-1]
            elif parts[0] == 'frappe':
                app_label = 'erp_core'
                func_name = parts[-1]
            else:
                return JsonResponse({'error': 'Unsupported method prefix'}, status=400)

            if app_label not in ALLOWED_APPS:
                return JsonResponse({'error': f'App {app_label} not in RPC whitelist'}, status=403)

            try:
                services_module = importlib.import_module(f'{app_label}.services')
                func = getattr(services_module, func_name)

                if not callable(func):
                    return JsonResponse({'error': f'{func_name} is not callable'}, status=400)

                # Execute the function stub
                result = func()

                return JsonResponse({
                    'message': f'Method {method_path} executed',
                    'status': 'success',
                    'result': result,
                    'resolved_to': f'{app_label}.services.{func_name}'
                })
            except (ImportError, AttributeError) as e:
                return JsonResponse({
                    'message': f'Method {method_path} not found in services layer',
                    'error': str(e),
                    'status': 'not_found'
                }, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)
