import requests

class EnsemblService:
    BASE_URL = "https://rest.ensembl.org/variation/human/"

    @staticmethod
    def get_variant_data(rsid):
        url = f"{EnsemblService.BASE_URL}{rsid}?content-type=application/json"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            return {
                "rsid": data.get("name", rsid),
                "chromosome": data.get("mappings", [{}])[0].get("seq_region_name", "N/A"),
                "position": data.get("mappings", [{}])[0].get("start", "N/A"),
                "alleles": data.get("mappings", [{}])[0].get("allele_string", "N/A"),
                "minor_allele_freq": data.get("MAF", "N/A"),
                "consequence": data.get("most_severe_consequence", "N/A"),
                "raw_data": data
            }
        except requests.exceptions.RequestException as e:
            # Verifica se o erro é 400 (geralmente RSID inexistente)
            if hasattr(e.response, 'status_code') and e.response.status_code == 400:
                msg = "O identificador não foi encontrado!"
            else:
                msg = "Ocorreu um problema de conexão com o servidor Ensembl!"

            return {
                "error": msg,
                "technical_details": str(e)  # Guarda o erro "feio" aqui
            }