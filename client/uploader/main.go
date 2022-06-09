package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type speedtestResultInput struct {
	SpeedtestResult speedtestResult `json:"speedtestResult"`
}

type operation struct {
	Query         string               `json:"query"`
	Variables     speedtestResultInput `json:"variables"`
	OperationName string               `json:"operationName"`
}

func main() {
	url := "http://0.0.0.0:8080/graphql"
	speedtestResultRaw, err := os.ReadFile("results.json")
	if err != nil {
		panic(err)
	}
	var data speedtestResult
	err = json.Unmarshal(speedtestResultRaw, &data)
	if err != nil {
		panic(err)
	}
	op := operation{
		OperationName: "mutation",
		Variables:     speedtestResultInput{SpeedtestResult: data},
		Query:         getQueryString(),
	}
	bod, err := json.Marshal(op)
	fmt.Println(string(bod))
	if err != nil {
		panic(err)
	}
	req, err := http.NewRequest("POST", url, bytes.NewReader(bod))
	if err != nil {
		panic(err)
	}
	req.Header.Set("user_ref", os.Getenv("TOKEN"))
	req.Header.Set("Content-Type", "application/json")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	respBody, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(respBody))
}
