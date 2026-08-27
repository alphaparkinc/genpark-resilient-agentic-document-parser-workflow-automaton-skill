from client import ResilientAgenticDocumentParserWorkflowAutomatonClient

def main():
    client = ResilientAgenticDocumentParserWorkflowAutomatonClient()
    res = client.parse_unstructured_document_stream('https://assets.genpark.ai/docs/healthcare_claim_form_hcfa.pdf', 'JSON_SCHEMA_V4')
    print('Automaton Run: ' + res['automaton_run_id'] + ' (' + str(res['document_pages_processed']) + ' pages processed)')
    print('Tables Extracted: ' + str(res['unstructured_tables_extracted']) + ' (OCR Confidence: ' + str(res['ocr_vision_extraction_confidence_pct']) + '%)')
    print('Schema Drift Remediated: ' + str(res['schema_drift_auto_remediated']) + ' | API Sync: ' + str(res['downstream_api_sync_completed']))
    print('Structured JSON: ' + res['structured_json_output_url'])

if __name__ == '__main__':
    main()
