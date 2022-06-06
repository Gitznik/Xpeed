import strawberry

from backend.storage.database import DbInterface


@strawberry.type
class Ping:
    jitter: float
    latency: float


@strawberry.type
class SpeedMeasurement:
    bandwidth: int
    bytes: int
    elapsed: int


@strawberry.type
class Interface:
    internalIp: str
    name: str
    macAddr: str
    isVpn: bool
    externalIp: str


@strawberry.type
class Server:
    id: int
    host: str
    port: int
    name: str
    location: str
    country: str
    ip: str


@strawberry.type
class Result:
    id: str
    url: str
    persisted: bool


@strawberry.type
class SpeedtestResult:
    type: str
    timestamp: str
    ping: "Ping"
    download: "SpeedMeasurement"
    upload: "SpeedMeasurement"
    packetLoss: int
    isp: str
    interface: "Interface"
    server: "Server"
    result: "Result"


@strawberry.input
class PingInput:
    jitter: float
    latency: float


@strawberry.input
class SpeedMeasurementInput:
    bandwidth: int
    bytes: int
    elapsed: int


@strawberry.input
class InterfaceInput:
    internalIp: str
    name: str
    macAddr: str
    isVpn: bool
    externalIp: str


@strawberry.input
class ServerInput:
    id: int
    host: str
    port: int
    name: str
    location: str
    country: str
    ip: str


@strawberry.input
class ResultInput:
    id: str
    url: str
    persisted: bool


@strawberry.input
class AddSpeedtestResultInput:
    type: str
    timestamp: str
    ping: "PingInput"
    download: "SpeedMeasurementInput"
    upload: "SpeedMeasurementInput"
    packetLoss: int
    isp: str
    interface: "InterfaceInput"
    server: "ServerInput"
    result: "ResultInput"


def store_speedtest_results(
    speedtest_result: AddSpeedtestResultInput, user_ref: str, db: DbInterface
) -> SpeedtestResult:
    parsed_result = SpeedtestResult(
        type=speedtest_result.type,
        timestamp=speedtest_result.timestamp,
        ping=Ping(
            jitter=speedtest_result.ping.jitter, latency=speedtest_result.ping.latency
        ),
        download=SpeedMeasurement(
            bandwidth=speedtest_result.download.bandwidth,
            bytes=speedtest_result.download.bytes,
            elapsed=speedtest_result.download.elapsed,
        ),
        upload=SpeedMeasurement(
            bandwidth=speedtest_result.upload.bandwidth,
            bytes=speedtest_result.upload.bytes,
            elapsed=speedtest_result.upload.elapsed,
        ),
        packetLoss=speedtest_result.packetLoss,
        isp=speedtest_result.isp,
        interface=Interface(
            internalIp=speedtest_result.interface.internalIp,
            name=speedtest_result.interface.name,
            macAddr=speedtest_result.interface.macAddr,
            isVpn=speedtest_result.interface.isVpn,
            externalIp=speedtest_result.interface.externalIp,
        ),
        server=Server(
            id=speedtest_result.server.id,
            host=speedtest_result.server.host,
            port=speedtest_result.server.port,
            name=speedtest_result.server.name,
            location=speedtest_result.server.location,
            country=speedtest_result.server.country,
            ip=speedtest_result.server.ip,
        ),
        result=Result(
            id=speedtest_result.result.id,
            url=speedtest_result.result.url,
            persisted=speedtest_result.result.persisted,
        ),
    )

    speedtest_dict = speedtest_result.__dict__
    for field in ["ping", "download", "upload", "interface", "server", "result"]:
        speedtest_dict[field] = speedtest_dict[field].__dict__
    
    storage_dict = {
        "data": speedtest_dict,
        "user_data": {
            "user_ref": user_ref,
        }
    }
    db.save_run_results(storage_dict)
    return parsed_result
