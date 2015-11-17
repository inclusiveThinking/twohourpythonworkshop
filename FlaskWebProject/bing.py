from tokens import * 

import urllib
import urllib2
import json
from flask_restful import Resource 

class Bing_Search(Resource):
	def search(self, search_type, query):
		key = bing_token
		query = urllib.quote(query)
		user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
		credentials = (':%s' % key).encode('base64')[:-1]
		auth = 'Basic %s' % credentials
		url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=5&$format=json'
		request = urllib2.Request(url)
		request.add_header('Authorization', auth)
		request.add_header('User-Agent', user_agent)
		request_opener = urllib2.build_opener()
		response = request_opener.open(request)
		response_data = response.read()
		json_result = json.loads(response_data)
		result_list = json_result['d']['results']
		print result_list
		return result_list