import pprint
from pylighthouse import LighthousePuller, DataPointsQuery
from datetime import datetime, timedelta

endTime_now = datetime.now()
startTime_delta = endTime_now - timedelta(minutes=15)

startTime = int(startTime_delta.timestamp())
endTime = int(endTime_now.timestamp())

cert_file = '/Users/dpaul/.certs/dpaul.crt'
cert_key =  '/Users/dpaul/.certs/dpaul.key'

query = DataPointsQuery(start_time=startTime, end_time=endTime)

#Here the script needs the certs
lighthouse_puller = LighthousePuller(cert=(cert_file,cert_key))  

data_points = lighthouse_puller.pull("mapper_sre","dnsp_ff_capacity_oversightKPI_load_ratio",query=query) 
print(data_points)

