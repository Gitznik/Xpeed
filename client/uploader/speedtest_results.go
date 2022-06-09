package main

type ping struct {
	Jitter  float64 `json:"jitter"`
	Latency float64 `json:"latency"`
}

type speedMeasure struct {
	Bandwidth float64 `json:"bandwidth"`
	Bytes     int     `json:"bytes"`
	Elapsed   int     `json:"elapsed"`
}

type internetInterface struct {
	InternalIp string `json:"internalIp"`
	Name       string `json:"name"`
	MacAddr    string `json:"macAddr"`
	IsVpn      bool   `json:"isVpn"`
	ExternalIp string `json:"externalIp"`
}

type server struct {
	Id       int    `json:"id"`
	Host     string `json:"host"`
	Port     int    `json:"port"`
	Name     string `json:"name"`
	Location string `json:"location"`
	Country  string `json:"country"`
	Ip       string `json:"ip"`
}

type result struct {
	Id         string `json:"id"`
	Url        string `json:"url"`
	Persistend bool   `json:"persisted"`
}

type speedtestResult struct {
	ReportType        string            `json:"type"`
	Timestamp         string            `json:"timestamp"`
	Ping              ping              `json:"ping"`
	Download          speedMeasure      `json:"download"`
	Upload            speedMeasure      `json:"upload"`
	PacketLoss        int               `json:"packetLoss"`
	Isp               string            `json:"isp"`
	InternetInterface internetInterface `json:"interface"`
	Server            server            `json:"server"`
	Result            result            `json:"result"`
}
