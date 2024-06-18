description = {
"AirConditioner":
'''Functions : [
    on(),
	off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
	switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags : [
    myroom,
    livingroom
]''',

"AirPurifier":
'''Functions : [
    on(),
	off(),
    setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
]
Values : [
	switch : string {"on"|"off"},
    airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
]
Tags : [
    kitchen,
    livingroom,
    bedroom
]''',

"AirQualityDetector":
'''Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags : [
    bedroom,
    livingroom,
    office
]''',

"Blind":
'''Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags : [
    bedroom,
    livingroom,
    office
]''',

"Button":
'''Functions : []
Values : [
    button : string {"pushed"|"held"|"double"|"pushed_2x"|"pushed_3x"|"pushed_4x"|"pushed_5x"|"pushed_6x"|"down"|"down_2x"|"down_3x"|"down_4x"|"down_5x"|"down_6x"|"down_hold"|"up"|"up_2x"|"up_3x"|"up_4x"|"up_5x"|"up_6x"|"up_hold"|"swipe_up"|"swipe_down"|"swipe_left"|"swipe_right"}
]
Tags : [
    sofa,
    bed,
    healing_mode,
    party_mode,
]''',

"Calculator":
'''Functions : [
    add(double, double) : return double,
    sub(double, double) : return double,
    div(double, double) : return double,
    mul(double, double) : return double,
    mod(double, double) : return double
]
Values : []''',

"Camera":
'''Functions : [
    on(),
	off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
	switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags : [
    livingroom,
    balcony,
    bedroom
]''',

"Charger":
'''Functions : [
    on(),
	off()
]
Values : [
    voltage : double,
    current : double,
	switch : string {"on"|"off"},
    chargingState : string {"charging"|"discharging"|"stopped"|"fullyCharged"|"error"}
]''',

"Clock":
'''Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]''',

"ContactSensor":
'''Functions : []
Values : [
    contact : string {"open"|"closed"}
]
Tags : [
    entrance,
    maindoor,
    backdoor,
    garage
]''',

"Curtain":
'''Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags : [
    myroom
]''',

"Dehumidifier":
'''Functions : [
    on(),
	off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
	switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags : [
    utilityroom,
    storage,
    laundryroom
]''',

"Dishwasher":
'''Functions : [
    on(),
	off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
	switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags : [
    kitchen
]''',

"DoorLock":
'''Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags : [
    entrance,
    maindoor,
    backdoor
]''',

"EmailProvider":
'''Functions : [
    sendMail(toAddress: string , title: string , text: string),
    sendMailWithFile(toAddress: string, title: string, text: string, filePath: string)
]
Values : []''',

"Fan":
'''Functions : [
    on(),
	off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
	switch : string {"on"|"off"},

]
Tags : [
    myroom,
    livingroom
]''',

"Feeder":
'''Functions : [
    on(),
	off(),
    startFeeding(),
    setFeedPortion(portion: double [0 ~ 2000], unit: string {"grams"|"pounds"|"ounces"|"servings"})
]
Values : [
	switch : string {"on"|"off"},
    feederOperatingState : string {"idle"|"feeding"|"error"}
]
Tags : [
    livingroom,
    kitchen,
    utilityroom
]''',

"GasMeter":
'''Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags : [
    kitchen
]''',

"GasValve":
'''Functions : [
	open(),
	close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags : [
    kitchen
]''',

"Humidifier":
'''Functions : [
    on(),
	off(),
    setHumidifierMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
	switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags : [
    myroom,
    livingroom
]''',

"HumiditySensor":
'''Functions : []
Values : [
    humidity : double[0 ~ 100]
]''',

"Irrigator":
'''Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values :	[
    switch: string {"on"|"off"}
]
Tags : [
    balcony,
    yard
]''',

"LeakSensor":
'''Functions : []
Values : [
    leakage : string {"detected"|"not_detected"}
]''',

"Light":
'''Functions : [
    on(),
	off(),
	setColor(color: string {"{hue}|{saturation}|{brightness}"})
	setLevel(level int [0 ~ 100])
]
Values : [
	switch : string {"on"|"off"},
	light : double
]
Tags : [
    myroom,
    balcony,
    entrance,
    bedroom,
    bathroom,
    livingroom,
    utilityroom,
    storage,
    garage
]''',

"LightSensor":
'''Functions : []
Values : [
    light : double
]''',

"MenuProvider":
'''Functions : [
    menu(command: string) : command format {"{오늘|내일} {학생식당|수의대식당|전망대(3식당)|예술계식당(아름드리)|기숙사식당|아워홈|동원관식당(113동)|웰스토리(220동)|투굿(공대간이식당)|자하연식당|301동식당} {아침|점심|저녁}"}
    todayMenu()
]
Values : []''',

"MotionSensor":
'''Functions : []
Values : [
    motion : string {"active"|"inactive"}
]
Tags : [
    myroom,
    balcony,
    entrance,
    bedroom,
    bathroom,
    livingroom,
    utilityroom,
    storage
]''',

"PresenceSensor":
'''Functions : []
Values : [
    presence : string {"present"|"not_present"}
]
Tags : [
    myroom,
    balcony,
    entrance,
    bedroom,
    bathroom,
    livingroom,
    utilityroom,
    storage
]''',

"Pump":
'''Functions : [
    on(),
	off(),
    setOperationMode(string mode {"normal"|"minimum"|"maximum"})
]
Values : [
	switch : string {"on"|"off"},
    operationMode : string {"normal"|"minimum"|"maximum"}
]
Tags : [
    balcony,
    garden
]''',

"Refrigerator":
'''Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"}) 
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]''',

"RobotCleaner":
'''Functions : [
    on(),
    off(),
    setRobotCleanerCleaningMode(string mode{"auto"|"part"|"repeat"|"manual"|"stop"|"map"})
]
Values : [
    switch : string {"on"|"off"},
    robotCleanerCleaningMode : string {"auto"|"part"|"repeat"|"manual"|"stop"|"map"}

]
Tags : [
    livingroom,
    storage
]''',

"Shade":
'''Functions : [
	open(),
	close(),
    setShadeLevel(openPercent: int[0 ~ 100])
]
Values : [
    shadeLevel : int openPercent[0 ~ 100]
]
Tags : [
    myroom,
    bathroom
]''',

"Siren":
'''Functions : [
    on(),
	off(),
    setSirenMode(mode: string {"both"|"off"|"siren"|"strobe"})
]
Values : [
	switch : string {"on"|"off"},
    sirenMode : string {"both"|"off"|"siren"|"strobe"}
]
Tags : [
    livingroom,
    entrance,
    garage
]''',

"SmartPlug":
'''Functions : [
    on(),
	off()
]
Values : [
	switch : string {"on"|"off"},
    chargingState : string {"charging"|"discharging"|"stopped"|"fullyCharged"|"error"},
    voltage : double,
    current : double
]''',

"SmokeDetector":
'''Functions : []
Values : [
    smoke : string {"detected"|"not_detected"} 
]
Tags : [
    myroom,
    balcony,
    bedroom,
    livingroom,
    utilityroom,
    storage,
    kitchen
]''',


"SoundSensor":
'''Functions : []
Values : [
    sound : string {"detected"|"not_detected"},
	soundPressureLevel : double [0 ~ 194]
]
''',

"Speaker":
'''Functions : [
    on(),
	off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
	switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags : [
    myroom,
    livingroom,
    yard
]''',

"Switch":
'''Functions : [
    on(),
	off()
]
Values : [
	switch : string {"on"|"off"}
]''',

"Television":
'''Functions : [
    on(),
	off(),
	setTvChannel(tvChannel: int),
	channelUp(),
	channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
	mute() : void, toggle muteStatus

Values : [
	switch : string {"on"|"off"}
	muteStatus : string {"muted"|"unmuted"}
	tvChannel : int
]
Tags : [
    myroom,
    livingroom,
    bedroom
]''',

"TemperatureSensor":
'''Functions : []
Values : [
    temperature: int [-460 ~ 10000]
]''',

"Valve":
'''Functions : [
    on(),
	off(),
    open(),
    close()
]
Values : [
    switch : str{"on"|"off"},
    valve : str{"closed"|"open"}
]''',

"WeatherProvider":
'''Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
	temperature : int celcius,
	humidity : double,
	pressure : double
]''',

"Window":
'''Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags : [
    myroom,
    balcony,
    bedroom,
    bathroom,
    livingroom,
    utilityroom
]'''
}