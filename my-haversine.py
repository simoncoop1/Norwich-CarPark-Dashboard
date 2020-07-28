import math

long1 = -1.45723343
lat1 = 52.27519523
long2 = -1.45723343
lat2 = 52.1
ψ1 = lat1 * (math.pi / 180)
ψ2 = lat2 * (math.pi/180)
λ1 = long1 * (math.pi/180)
λ2 = long2 * (math.pi/180)
Δψ = ψ2 - ψ1
Δλ = λ2 - λ1
R = 6371 # radius of earth (km)

a = (math.sin(Δψ/2) **2) + (math.cos(ψ1) * math.cos(ψ2) * (math.sin(Δλ/2) **2))
c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
d = R * c

print("distance is",d,"(km)")

