import pytest
from tfl_arrivals.parse_arrivals import parse_arrivals
from tfl_arrivals.arrival_data import Arrival, StopId, VehicleId
from datetime import datetime


def test_parse():    
    raw_json = """[{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-526541792","operationType":1,"vehicleId":"227","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUUXB","destinationName":"Uxbridge Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":226,"currentLocation":"At Green Park Platform 1","towards":"Uxbridge","expectedArrival":"2018-02-14T12:07:21Z","timeToLive":"2018-02-14T12:07:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.512Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"1451143100","operationType":1,"vehicleId":"233","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHR4","destinationName":"Heathrow Terminal 4 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":946,"currentLocation":"At Caledonian Road Platform 2","towards":"Heathrow via T4 Loop","expectedArrival":"2018-02-14T12:19:21Z","timeToLive":"2018-02-14T12:19:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.558Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"768443754","operationType":1,"vehicleId":"235","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHR4","destinationName":"Heathrow Terminal 4 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":286,"currentLocation":"At Piccadilly Circus Platform 4","towards":"Heathrow via T4 Loop","expectedArrival":"2018-02-14T12:08:21Z","timeToLive":"2018-02-14T12:08:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.512Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"902191899","operationType":1,"vehicleId":"242","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLURYL","destinationName":"Rayners Lane Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":646,"currentLocation":"At Russell Square Platform 2","towards":"Rayners Lane","expectedArrival":"2018-02-14T12:14:21Z","timeToLive":"2018-02-14T12:14:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.543Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-2003488047","operationType":1,"vehicleId":"244","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLURYL","destinationName":"Rayners Lane Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1606,"currentLocation":"Between Wood Green and Turnpike Lane","towards":"Rayners Lane","expectedArrival":"2018-02-14T12:30:21Z","timeToLive":"2018-02-14T12:30:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.605Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-526672864","operationType":1,"vehicleId":"247","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHRC","destinationName":"Heathrow Terminals 1-2-3 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1426,"currentLocation":"Between Turnpike Lane and Manor House","towards":"Heathrow T123 + 5","expectedArrival":"2018-02-14T12:27:21Z","timeToLive":"2018-02-14T12:27:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.59Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"1315113359","operationType":1,"vehicleId":"256","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHRC","destinationName":"Heathrow Terminals 1-2-3 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":77,"currentLocation":"At Hyde Park Corner Platform 2","towards":"Heathrow T123 + 5","expectedArrival":"2018-02-14T12:04:52Z","timeToLive":"2018-02-14T12:04:52Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.496Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"2114669666","operationType":1,"vehicleId":"300","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHR4","destinationName":"Heathrow Terminal 4 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":766,"currentLocation":"At King's Cross Platform 5","towards":"Heathrow via T4 Loop","expectedArrival":"2018-02-14T12:16:21Z","timeToLive":"2018-02-14T12:16:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.543Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-1868377977","operationType":1,"vehicleId":"301","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUHRC","destinationName":"Heathrow Terminals 1-2-3 Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":586,"currentLocation":"Between Russell Square and Holborn","towards":"Heathrow T123 + 5","expectedArrival":"2018-02-14T12:13:21Z","timeToLive":"2018-02-14T12:13:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.527Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"903502616","operationType":1,"vehicleId":"302","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUUXB","destinationName":"Uxbridge Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1786,"currentLocation":"At Wood Green Sidings","towards":"Uxbridge","expectedArrival":"2018-02-14T12:33:21Z","timeToLive":"2018-02-14T12:33:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.621Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-2003422506","operationType":1,"vehicleId":"334","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUNFD","destinationName":"Northfields Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1306,"currentLocation":"At Finsbury Park Platform 3","towards":"Northfields","expectedArrival":"2018-02-14T12:25:21Z","timeToLive":"2018-02-14T12:25:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.59Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"902126360","operationType":1,"vehicleId":"352","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUNFD","destinationName":"Northfields Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1066,"currentLocation":"At Holloway Road Platform 1","towards":"Northfields","expectedArrival":"2018-02-14T12:21:21Z","timeToLive":"2018-02-14T12:21:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.574Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}},{"$type":"Tfl.Api.Presentation.Entities.Prediction, Tfl.Api.Presentation.Entities","id":"-2003619114","operationType":1,"vehicleId":"364","naptanId":"940GZZLUKNB","stationName":"Knightsbridge Underground Station","lineId":"piccadilly","lineName":"Piccadilly","platformName":"Westbound - Platform 2","direction":"inbound","bearing":"","destinationNaptanId":"940GZZLUUXB","destinationName":"Uxbridge Underground Station","timestamp":"2018-02-14T12:03:35Z","timeToStation":1126,"currentLocation":"At Arsenal Platform 2","towards":"Uxbridge","expectedArrival":"2018-02-14T12:22:21Z","timeToLive":"2018-02-14T12:22:21Z","modeName":"tube","timing":{"$type":"Tfl.Api.Presentation.Entities.PredictionTiming, Tfl.Api.Presentation.Entities","countdownServerAdjustment":"00:00:00","source":"0001-01-01T00:00:00","insert":"0001-01-01T00:00:00","read":"2018-02-14T12:03:31.574Z","sent":"2018-02-14T12:03:35Z","received":"0001-01-01T00:00:00"}}]"""    
    arrivals = parse_arrivals(raw_json)
    expected = [
        Arrival(arrival_id=-526541792, vehicle_id=VehicleId(227), naptan_id=StopId("940GZZLUKNB"), towards="Uxbridge", expected=datetime(2018, 2, 14, 12, 7, 21), ttl=datetime(2018, 2, 14, 12, 7, 21)),
        Arrival(arrival_id=1451143100, vehicle_id=VehicleId(233), naptan_id=StopId("940GZZLUKNB"), towards="Heathrow via T4 Loop", expected=datetime(2018, 2, 14, 12, 19, 21), ttl=datetime(2018, 2, 14, 12, 19, 21)),
        Arrival(arrival_id=768443754, vehicle_id=VehicleId(235), naptan_id=StopId("940GZZLUKNB"), towards="Heathrow via T4 Loop", expected=datetime(2018, 2, 14, 12,  8, 21), ttl=datetime(2018, 2, 14, 12,  8, 21)),
        Arrival(arrival_id=902191899, vehicle_id=VehicleId(242), naptan_id=StopId("940GZZLUKNB"), towards="Rayners Lane", expected=datetime(2018, 2, 14, 12, 14, 21), ttl=datetime(2018, 2, 14, 12, 14, 21))
        ]
    assert arrivals[:4] == expected

