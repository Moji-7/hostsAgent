jq .uptime ../../../checklist/response/s1shetab_s1*_infoUptime-fn.json | jq .server,.value
CM1,CM2
kish=s2
ferd=s3
jq .uptime ../../../checklist/response/s1shaparak_s1shap*_infoUptime-fn.json | jq .server,.value
jq .uptime ../../../checklist/response/s3shaparak_"s3*_infoUptime-fn.json | jq .server,.value
CM1,CM2
macna,oroush,harim.sama,iwa
jq .uptime ../../../checklist/response/soroush_*_infoUptime-fn.json | jq .server,.value


