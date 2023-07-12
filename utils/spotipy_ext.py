import logging 
from spotipy.oauth2 import SpotifyOAuth, SpotifyStateError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CustomSpotifyOAuth(SpotifyOAuth):
    """ 
    Custom wrapper to allow the bot to authenticate itself.
    User Landon Turner has given permission with use of Bardic Inspiration
    """

    def _get_auth_response_interactive(self, open_browser=False):
        if open_browser:
            raise Exception("Custom class was intenrally misconfigured")
        else:
            url = self.get_authorize_url()
        logger.info(f"!!!!!!!!!!!!! 'authorized url' {url}")
        state, code = SpotifyOAuth.parse_auth_response_url(url)
        if self.state is not None and self.state != state:
            raise SpotifyStateError(self.state, state)
        return code