import json

class yiTimeSeries:
    def __init__(self):
        print "Create pyadder"

    def aggregate(self, data):
        data_json = json.loads(data)
        output = data_json['data']['time_series']['numberArray1']
        timestamps = data_json['data']['time_series']['time_stamp']
        return json.dumps( \
            {
                "data":
                    {
                        "time_series":
                            {
                                "time_stamp": timestamps,
                                "aggregation": output
                            }
                    }
            })
