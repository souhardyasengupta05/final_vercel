from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import math
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

class LatencyRequest(BaseModel):
    regions: List[str]
    threshold_ms: float

# Telemetry data assigned to a variable
TELEMETRY_DATA = [
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 182.47,
    "uptime_pct": 98.159,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 199.69,
    "uptime_pct": 97.571,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 184.49,
    "uptime_pct": 97.393,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 121.33,
    "uptime_pct": 98.897,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 203.84,
    "uptime_pct": 99.401,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 206.67,
    "uptime_pct": 98.052,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 125.32,
    "uptime_pct": 97.56,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 146.82,
    "uptime_pct": 98.059,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 139.79,
    "uptime_pct": 98.601,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 210.69,
    "uptime_pct": 98.089,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 222.44,
    "uptime_pct": 98.685,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 170.4,
    "uptime_pct": 97.36,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 235.47,
    "uptime_pct": 99.293,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 136.27,
    "uptime_pct": 99.369,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 160.79,
    "uptime_pct": 97.612,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 213.12,
    "uptime_pct": 99.092,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 155.9,
    "uptime_pct": 99.011,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 158.46,
    "uptime_pct": 97.315,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "analytics",
    "latency_ms": 124.32,
    "uptime_pct": 98.785,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 170.75,
    "uptime_pct": 99.414,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 114.39,
    "uptime_pct": 98.863,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 138.23,
    "uptime_pct": 98.309,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 125.86,
    "uptime_pct": 97.839,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 225,
    "uptime_pct": 97.849,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 131.48,
    "uptime_pct": 97.983,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 138.49,
    "uptime_pct": 98.232,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 122.98,
    "uptime_pct": 97.697,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 166.72,
    "uptime_pct": 97.609,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 198.09,
    "uptime_pct": 98.813,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "checkout",
    "latency_ms": 199.96,
    "uptime_pct": 98.216,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 196.31,
    "uptime_pct": 98.503,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 148.33,
    "uptime_pct": 98.79,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 211.25,
    "uptime_pct": 97.408,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 217.29,
    "uptime_pct": 98.711,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 215.75,
    "uptime_pct": 99.182,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 153.86,
    "uptime_pct": 98.729,
    "timestamp": 20250312
  }
]

def calculate_percentile(data: List[float], percentile: float) -> float:
    """Calculate the nth percentile for a list of values"""
    if not data:
        return 0.0
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    index = (percentile / 100) * (n - 1)
    
    if index.is_integer():
        return sorted_data[int(index)]
    else:
        lower_index = math.floor(index)
        upper_index = math.ceil(index)
        lower_value = sorted_data[lower_index]
        upper_value = sorted_data[upper_index]
        weight = index - lower_index
        return lower_value + (upper_value - lower_value) * weight

@app.post("/")
async def calculate_latency_metrics(request: LatencyRequest) -> Dict[str, Any]:
    """
    Calculate latency metrics for specified regions
    """
    try:
        results = {}
        
        for region in request.regions:
            # Filter data for the current region
            region_data = [item for item in TELEMETRY_DATA if item["region"] == region]
            
            if not region_data:
                results[region] = {
                    "avg_latency": 0.0,
                    "p95_latency": 0.0,
                    "avg_uptime": 0.0,
                    "breaches": 0
                }
                continue
            
            # Extract latency and uptime values
            latencies = [item["latency_ms"] for item in region_data]
            uptimes = [item["uptime_pct"] for item in region_data]
            
            # Calculate metrics
            avg_latency = sum(latencies) / len(latencies)
            p95_latency = calculate_percentile(latencies, 95)
            avg_uptime = sum(uptimes) / len(uptimes)
            breaches = sum(1 for latency in latencies if latency > request.threshold_ms)
            
            results[region] = {
                "avg_latency": round(avg_latency, 2),
                "p95_latency": round(p95_latency, 2),
                "avg_uptime": round(avg_uptime, 2),
                "breaches": breaches
            }
        
        return {"regions": results}
    
    except Exception as e:
        return {"error": f"Error processing request: {str(e)}"}

@app.get("/")
async def root():
    return {"message": "Latency Metrics API", "instructions": "Send POST request to / with JSON body: {'regions': ['region1', 'region2'], 'threshold_ms': 180}"}

@app.options("/")
async def options():
    return {"message": "OK"}

# Vercel requires this
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
