package main

func getQueryString() string {
	return `query mutation($speedtestResult: AddSpeedtestResultInput!) {
		storeSpeedtestResults(speedtestResult: $speedtestResult) {
		  type
		  timestamp
		  ping {
			jitter
			latency
		  }
		  download {
			bandwidth
			bytes
			elapsed
		  }
		  upload {
			bandwidth
			bytes
			elapsed
		  }
		  packetLoss
		  isp
		  interface {
			internalIp
			name
			macAddr
			isVpn
			externalIp
		  }
		  server {
			id
			host
			port
			name
			location
			country
			ip
		  }
		  result {
			id
			url
			persisted
		  }
		}
	  }
	  `
}
