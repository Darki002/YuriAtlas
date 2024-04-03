from .recommendation_system import RecommendationEngine
from yuri_manga_spreadsheet import spreadsheet_access
from readinglist import user_readinglist
from readinglist.websites import Websites
from yuri_manga_processing.yuri_manga import YuriManga
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def recommend_for(user_name: str, platform: Websites) -> list[YuriManga] | None:
    """
    Creates a recommendation list for a user based on their reading list.
    :param user_name: The username on the platform the user chose.
    :param platform: The platform of user's reading list.
    :return: A list of YuriManga objects or None if an error occurred.
    """

    try:
        user_reading_list = user_readinglist.get_user_list_from(user_name, platform)
    except Exception as e:
        logger.error(f"Failed to retrieve data for User {user_name} from source {platform.value}. Error: {e}")
        return None

    spreadsheet = spreadsheet_access.get_all()
    if spreadsheet is None:
        return None

    recommendation_engine = RecommendationEngine(user_reading_list, spreadsheet)
    recommendation_engine.set_up()

    return recommendation_engine.create_recommendation()
