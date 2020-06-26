"""Octopus Energy API Class"""
from .request_api import RequestAPI

class OctoAPI(RequestAPI):
	def __init__(
		self, api_key: str,
	):
		"""Constructor requires API-KEY

      Args:
        api_key: API key from Octopus Energy.
    """
		super().__init__(api_key)

	def electricity_meter_point(self, mpan):
		""" See https://developer.octopus.energy/docs/api/#electricity-meter-points """
		
		return self.request_get(f"/electricity-meter-points/{mpan}/")
