import json

from src.data_processing.data_processing import data_processing
from src.data_processing.json_unifier import json_formatter
from src.database.query import get_document
from src.web_scraper.real_time_data_scraper.spider_run import RunSpider


def run_report_generator(country, league, team):
    # Query database

    document = get_document(country, league, team)

    # Run Scraper

    RunSpider.run_spider_and_get_result(team)

    # Get scraper json

    scraper_json_path = 'src/web_scraper/real_time_data_scraper/team_data.json'

    with open(scraper_json_path, 'r') as file:
        data = json.load(file)

    scraper_json = data[0]

    # Format jsons

    formatted_json = json_formatter(document, scraper_json)

    data_processing(formatted_json, 'src/view_pages/report/template.html')



country = "brazil_teams"
league = "serie_a"
team_name = "Sport Club Corinthians Paulista"

