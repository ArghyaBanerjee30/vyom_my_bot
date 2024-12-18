from urllib.parse import urlparse, parse_qs

def convert_to_csv_url(url: str) -> str:
    parsed_url = urlparse(url)

    sheet_id = parsed_url.path.split('/')[3]

    gid = parse_qs(parsed_url.query).get("gid", ["0"])[0]

    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    return csv_url