def get_content_sheet(service, spreadsheet_id: str, range_: str) -> list:
    try:
        return service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_).execute().get('values')
    except Exception as e:
        print(e)
        exit()


def get_columns(fields, necessary_fields) -> dict:
    columns = {}
    for field in necessary_fields:
        if field in fields:
            columns[field] = fields.index(field)

    return columns