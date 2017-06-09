# Predix-AnalyticFramework-yi-Demo
This is the demo for Predix-AnalyticFramework


Also this is a simple tutorial for the AnalyticFramework of GE Predix Platform.


The official tutorial is not perfect due to the swtich from Analytic Catalog, Analytic Runtime, Analytic Ui to AnalyticFramework.


The mixed tutorial has some out of date information about how to configure the AnalyticFramework.

# Quick Setup
Basically speaking, the Analyticframework is the combination of Analytic Catalog, Analytic Runtime, Analytic Ui. The following steps can
quickly guide you through some common issues.


1. Set up your own UAA service, Timeserise service.
2. In your UAA service, you should configure a UI client, a Runtime client and a Analyticferamework client. The corresponding authority and
scope please refer to [here](https://docs.predix.io/en-US/content/service/analytics_services/analytics_framework/get-started)
3. Subscribe the service in your Predix account and bind your UAA clients.
4. After your subscription, you should update your service with your timeseriesZoneID(also assetZoneID if you need) using cf command with
the following format.
'''json
{
     "trustedIssuerIds":[
         "UAA-URL"
     ],
     "runtimeDependentServices":{
         "predixTimeseriesZoneId": "yourTimeSeriesZoneID"
     },
     "uiDomainPrefix": "yourUiPrefix",
     "uiTrustedClientCredentials":{     
     "clientId": "yourUiClientID",
     "clientSecret": "yourUiClientSecret"
     },
     "runtimeTrustedClientCredentials":{
     "clientId": "yourSchedulerClient",
     "clientSecret" : "yourSchedulerClientSecret"
     }
 }
'''
5. After this you can upload your analytic code and an analytic template using the AnalyticUi following the [instruction](https://docs.predix.io/en-US/content/service/analytics_services/analytics_framework/analytic-management)

analytic tempalte defines the input & output data format of your code.
6. Then upload the Orchestration file which defines how your analytic code will be excuted during the runtime.
7. Upload the port-to-field file which defines how to process the data from the binded TimeSeries service.
8. Finally you can run the code using Postman.

The 6-7 steps can be finished using [Postman collection](https://github.com/PredixDev/predix-analytics-sample/blob/master/orchestrations/oneStepOrchestration/SingleStepOrchestrationDemoUsingTagMap.postman_collection.json)
In postman command, you can use the following request body to map data from TimeSeries to your Analytic code.
'''json
{
     "orchestrationConfigurationId": "orchestrationentryID",
     "assetId": null,
     "assetDataFieldsMap": {
         "temperature sensor": "tag-C", map tag-C from timeseries service to temperature sensor, and the analytic template will map this to your code input
         "demo aggregation": "demo-aggregation1h"
     },
     "assetGroup": null
 }
 '''
