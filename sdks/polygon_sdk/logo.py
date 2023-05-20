from urllib.parse import unquote
import aiohttp

async def get_polygon_logo(symbol):
    url = f'https://api.polygon.io/v3/reference/tickers/{symbol}?apiKey={poly_key2}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            
            if 'results' not in data:
                # No results found
                return None
            
            results = data['results']
            branding = results.get('branding')

            if branding and 'icon_url' in branding:
                encoded_url = branding['icon_url']
                decoded_url = unquote(encoded_url)
                url_with_api_key = f"{decoded_url}?apiKey={poly_key2}"
                return url_with_api_key
