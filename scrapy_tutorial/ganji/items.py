# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    carinfo0 = scrapy.Field()
    carinfo1 = scrapy.Field()
    carinfo2 = scrapy.Field()
    carinfo3 = scrapy.Field()
    carinfo4 = scrapy.Field()
    carinfo5 = scrapy.Field()
    carinfo6 = scrapy.Field()
    carinfo7 = scrapy.Field()
    carinfo8 = scrapy.Field()
    carinfo9 = scrapy.Field()
    carinfo10 = scrapy.Field()
    carinfo11 = scrapy.Field()
    carinfo12 = scrapy.Field()
    carinfo13 = scrapy.Field()
    carinfo14 = scrapy.Field()
    carinfo15 = scrapy.Field()
    carinfo16 = scrapy.Field()
    brandname = scrapy.Field()
    brandid = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    salesdesc = scrapy.Field()
    carid = scrapy.Field()
    makeyear = scrapy.Field()
    producestatus = scrapy.Field()
    salestatus = scrapy.Field()
    type = scrapy.Field()
    price = scrapy.Field()
    output = scrapy.Field()
    geartype = scrapy.Field()
    gearnum = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    wheel = scrapy.Field()
    weight = scrapy.Field()
    method = scrapy.Field()
    maxps = scrapy.Field()
    emission = scrapy.Field()
    fueltype = scrapy.Field()
    fuelnumber = scrapy.Field()
    assitanttype = scrapy.Field()
    backhang = scrapy.Field()
class AutohomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    jsonsave = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    carid = scrapy.Field()
    salesdesc = scrapy.Field()
    price = scrapy.Field()
    factoryname = scrapy.Field()
    type = scrapy.Field()
    motor = scrapy.Field()
    gear = scrapy.Field()
    lengthwh = scrapy.Field()
    body = scrapy.Field()
    maxspeed = scrapy.Field()
    accelerate = scrapy.Field()
    actualaccelerate = scrapy.Field()
    actualstop = scrapy.Field()
    actualpetrol = scrapy.Field()
    petrol = scrapy.Field()
    actual_liftoff_distance = scrapy.Field()
    warranty = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    wheel = scrapy.Field()
    frontwheel = scrapy.Field()
    backwheel = scrapy.Field()
    liftoff_distance = scrapy.Field()
    weight = scrapy.Field()
    body = scrapy.Field()
    doors = scrapy.Field()
    seats = scrapy.Field()
    fuelvolumn = scrapy.Field()
    baggage = scrapy.Field()
    motortype = scrapy.Field()
    cylinder = scrapy.Field()
    output = scrapy.Field()
    method = scrapy.Field()
    lwv = scrapy.Field()
    lwvnumber = scrapy.Field()
    valve = scrapy.Field()
    compress = scrapy.Field()
    valve_gear = scrapy.Field()
    cylinder_diameter = scrapy.Field()
    cylinder_travel = scrapy.Field()
    maxps = scrapy.Field()
    maxpower = scrapy.Field()
    maxrpm = scrapy.Field()
    maxnm = scrapy.Field()
    maxtorque = scrapy.Field()
    motortechnique = scrapy.Field()
    fuletype = scrapy.Field()
    fulevolumn = scrapy.Field()
    fulemethod = scrapy.Field()
    cylinder_head_material = scrapy.Field()
    cylinder_body_material = scrapy.Field()
    emission = scrapy.Field()
    geardesc = scrapy.Field()
    gearnumber = scrapy.Field()
    geartype = scrapy.Field()
    driveway = scrapy.Field()
    frontgauge = scrapy.Field()
    backgauge = scrapy.Field()
    assistanttype = scrapy.Field()
    body_structure = scrapy.Field()
    frontbrake = scrapy.Field()
    backbrake = scrapy.Field()
    parking_brake_type = scrapy.Field()
    frontwheel = scrapy.Field()
    backwheel = scrapy.Field()
    sparewheel = scrapy.Field()

class XcarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    brandname=scrapy.Field()
    brandid=scrapy.Field()
    factoryname=scrapy.Field()
    factoryid=scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    carid = scrapy.Field()
    salesdesc = scrapy.Field()
    makeyear = scrapy.Field()
    price = scrapy.Field()
    an_price = scrapy.Field()
    bname = scrapy.Field()
    type_name = scrapy.Field()
    disl_working_mpower = scrapy.Field()
    dynamic = scrapy.Field()
    speed_transtype = scrapy.Field()
    length_width_height = scrapy.Field()
    door_seat_frame = scrapy.Field()
    ear = scrapy.Field()
    mspeed = scrapy.Field()
    hatime = scrapy.Field()
    comfuel = scrapy.Field()
    ypolicy = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    wheelbase = scrapy.Field()
    weight = scrapy.Field()
    clearance = scrapy.Field()
    btread = scrapy.Field()
    ftread = scrapy.Field()
    frame = scrapy.Field()
    door = scrapy.Field()
    seat = scrapy.Field()
    oilbox = scrapy.Field()
    trunk = scrapy.Field()
    mtrunk = scrapy.Field()
    enginetype = scrapy.Field()
    disl = scrapy.Field()
    mdisl = scrapy.Field()
    working = scrapy.Field()
    cyarrange = scrapy.Field()
    cylinder = scrapy.Field()
    cylindernum = scrapy.Field()
    cr = scrapy.Field()
    valvegear = scrapy.Field()
    cylinderbore = scrapy.Field()
    journey = scrapy.Field()
    cylinderblock = scrapy.Field()
    cylinderhead = scrapy.Field()
    mhpower = scrapy.Field()
    mpower = scrapy.Field()
    mtorque = scrapy.Field()
    fuel = scrapy.Field()
    fuelno = scrapy.Field()
    sfueltype = scrapy.Field()
    envstand = scrapy.Field()
    stechnology = scrapy.Field()
    speed = scrapy.Field()
    transtype = scrapy.Field()
    tranname = scrapy.Field()
    drivetype = scrapy.Field()
    awdtype = scrapy.Field()
    mdifferentialtype = scrapy.Field()
    carstruc = scrapy.Field()
    hptype = scrapy.Field()
    fsustype_text = scrapy.Field()
    bsustype_text = scrapy.Field()
    fdifferentiallock = scrapy.Field()
    mdifferentiallock = scrapy.Field()
    rdifferentiallock = scrapy.Field()
    fbraketype = scrapy.Field()
    bbraketype = scrapy.Field()
    park = scrapy.Field()
    ftiresize = scrapy.Field()
    btiresize = scrapy.Field()
    sparetire = scrapy.Field()
    isdairbag = scrapy.Field()
    isfhairbag = scrapy.Field()
    isfsairbag = scrapy.Field()
    iskairbag = scrapy.Field()
    pedeairbag = scrapy.Field()
    isofix = scrapy.Field()
    istpmonitor = scrapy.Field()
    istpruning = scrapy.Field()
    isseatbeltti = scrapy.Field()
    iseanti = scrapy.Field()
    enginelock = scrapy.Field()
    iscclock = scrapy.Field()
    isrekey = scrapy.Field()
    baws = scrapy.Field()
    nightwork = scrapy.Field()
    isabs = scrapy.Field()
    isebd = scrapy.Field()
    iseba = scrapy.Field()
    isasr = scrapy.Field()
    isesp = scrapy.Field()
    hillassist = scrapy.Field()
    hdc = scrapy.Field()
    isuphillassist = scrapy.Field()
    isandstitch = scrapy.Field()
    deviatewar = scrapy.Field()
    iskbsus = scrapy.Field()
    issteesys = scrapy.Field()
    aba = scrapy.Field()
    iswindow = scrapy.Field()
    isarwindow = scrapy.Field()
    isspround = scrapy.Field()
    isaluhub = scrapy.Field()
    eletric_sdoor = scrapy.Field()
    electricdoor = scrapy.Field()
    rack = scrapy.Field()
    agrille = scrapy.Field()
    elecartrunk = scrapy.Field()
    isleasw = scrapy.Field()
    isswud = scrapy.Field()
    ismultisw = scrapy.Field()
    steelectrol = scrapy.Field()
    steewhmory = scrapy.Field()
    iswheelhot = scrapy.Field()
    isswshift = scrapy.Field()
    isassibc = scrapy.Field()
    isparkvideo = scrapy.Field()
    panorcamera = scrapy.Field()
    ispark = scrapy.Field()
    isascd = scrapy.Field()
    autcruise = scrapy.Field()
    isnokeyinto = scrapy.Field()
    isnokeysys = scrapy.Field()
    display = scrapy.Field()
    ishud = scrapy.Field()
    isleaseat = scrapy.Field()
    sportseat = scrapy.Field()
    isseatadj = scrapy.Field()
    isfseatadj = scrapy.Field()
    reseateletrol = scrapy.Field()
    iswaistadj = scrapy.Field()
    shouldersdj = scrapy.Field()
    thighsdj = scrapy.Field()
    iseseatmem = scrapy.Field()
    isseathot = scrapy.Field()
    isseatknead = scrapy.Field()
    chairmassage = scrapy.Field()
    secseatbadj = scrapy.Field()
    secseatfbwadj = scrapy.Field()
    isbseatlay = scrapy.Field()
    isbseatplay = scrapy.Field()
    thirdrowseat = scrapy.Field()
    isfarmrest = scrapy.Field()
    isbcup = scrapy.Field()
    isgps = scrapy.Field()
    isbluetooth = scrapy.Field()
    iscclcd = scrapy.Field()
    isblcd = scrapy.Field()
    humancomption = scrapy.Field()
    interservice = scrapy.Field()
    istv = scrapy.Field()
    audio_brand = scrapy.Field()
    aux = scrapy.Field()
    ismp3 = scrapy.Field()
    isscd = scrapy.Field()
    ismcd = scrapy.Field()
    allcd = scrapy.Field()
    onedvd = scrapy.Field()
    ismdvd = scrapy.Field()
    is2audio = scrapy.Field()
    is4audio = scrapy.Field()
    is6audio = scrapy.Field()
    is8audio = scrapy.Field()
    isxelamp = scrapy.Field()
    isledlamp = scrapy.Field()
    isjglamp = scrapy.Field()
    ishfoglamp = scrapy.Field()
    dayrunlight = scrapy.Field()
    islampheiadj = scrapy.Field()
    isautohlamp = scrapy.Field()
    bendauxlig = scrapy.Field()
    isturnhlamp = scrapy.Field()
    islampclset = scrapy.Field()
    interatmlamp = scrapy.Field()
    isfewindow = scrapy.Field()
    isgnhand = scrapy.Field()
    ispreventionuv = scrapy.Field()
    fseat_pglass = scrapy.Field()
    isermirror = scrapy.Field()
    ishotrmirror = scrapy.Field()
    iseprmirror = scrapy.Field()
    ecm = scrapy.Field()
    ismemorymirror = scrapy.Field()
    isbssvisor = scrapy.Field()
    ishbsvisor = scrapy.Field()
    issvisordr = scrapy.Field()
    isinswiper = scrapy.Field()
    rwiper = scrapy.Field()
    isairc = scrapy.Field()
    isaairc = scrapy.Field()
    fseat_ac = scrapy.Field()
    isbsairo = scrapy.Field()
    istempdct = scrapy.Field()
    isairfilter = scrapy.Field()
    iscaricebox = scrapy.Field()
    other = scrapy.Field()
class PcautoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    jsonsave = scrapy.Field()
    brandname= scrapy.Field()
    brandid = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    carid = scrapy.Field()
    salesdesc = scrapy.Field()
    price = scrapy.Field()
    level = scrapy.Field()
    salemonth = scrapy.Field()
    motor = scrapy.Field()
    method = scrapy.Field()
    maxps = scrapy.Field()
    maxnm = scrapy.Field()
    gear = scrapy.Field()
    bodystyle = scrapy.Field()
    lengthwh = scrapy.Field()
    wheel = scrapy.Field()
    maxspeed = scrapy.Field()
    accelerate = scrapy.Field()
    actualaccelerate = scrapy.Field()
    actualstop = scrapy.Field()
    petrol = scrapy.Field()
    warranty = scrapy.Field()
    type = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    wheel = scrapy.Field()
    frontwheel = scrapy.Field()
    backwheel = scrapy.Field()
    liftoff_distance = scrapy.Field()
    weight = scrapy.Field()
    doors = scrapy.Field()
    seats = scrapy.Field()
    fuelvolumn = scrapy.Field()
    baggage = scrapy.Field()
    maxbaggage = scrapy.Field()
    motortype = scrapy.Field()
    cylinder = scrapy.Field()
    method1 = scrapy.Field()
    maxps1 = scrapy.Field()
    maxpower = scrapy.Field()
    maxrpm = scrapy.Field()
    maxnm1 = scrapy.Field()
    maxtorque = scrapy.Field()
    lwv = scrapy.Field()
    lwvnumber = scrapy.Field()
    valve = scrapy.Field()
    compress = scrapy.Field()
    valve_gear = scrapy.Field()
    cylinder_diameter = scrapy.Field()
    cylinder_travel = scrapy.Field()
    motortechnique = scrapy.Field()
    fuletype = scrapy.Field()
    fulevolumn = scrapy.Field()
    fulemethod = scrapy.Field()
    cylinder_head_material = scrapy.Field()
    cylinder_body_material = scrapy.Field()
    emission = scrapy.Field()
    geardesc = scrapy.Field()
    gearnumber = scrapy.Field()
    geartype = scrapy.Field()
    driveway = scrapy.Field()
    frontgauge = scrapy.Field()
    backgauge = scrapy.Field()
    assistanttype = scrapy.Field()
    body_structure = scrapy.Field()
    frontbrake = scrapy.Field()
    backbrake = scrapy.Field()
    parking_brake_type = scrapy.Field()
    frontwheel = scrapy.Field()
    backwheel = scrapy.Field()
    sparewheel = scrapy.Field()
    approach_angle = scrapy.Field()
    departure_angle = scrapy.Field()
    ramp_angle = scrapy.Field()
    climbing_angle = scrapy.Field()
    liftoff_distance1 = scrapy.Field()
    turning_radius = scrapy.Field()
    wading_depth = scrapy.Field()
class QQItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    jsonsave = scrapy.Field()
    brandname= scrapy.Field()
    brandid = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    carid=scrapy.Field()
    salesdesc = scrapy.Field()
    carid = scrapy.Field()
class cheshiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    datasave = scrapy.Field()
    jsonsave = scrapy.Field()
    brandname= scrapy.Field()
    brandid = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    carid=scrapy.Field()
    salesdesc = scrapy.Field()
    price = scrapy.Field()
    makeyear = scrapy.Field()

class iautosItem(scrapy.Item):
        # define the fields for your item here like:
        # name = scrapy.Field()
        url = scrapy.Field()
        website = scrapy.Field()
        grabtime = scrapy.Field()
        status = scrapy.Field()
        datasave = scrapy.Field()
        brandname = scrapy.Field()
        brandid = scrapy.Field()
        factoryname = scrapy.Field()
        factoryid = scrapy.Field()
        familyname = scrapy.Field()
        familyid = scrapy.Field()
        carid = scrapy.Field()
        salesdesc = scrapy.Field()
        price = scrapy.Field()
        saleprice=scrapy.Field()
        price1_north=scrapy.Field()
        price1_east= scrapy.Field()
        price1_west= scrapy.Field()
        price1_south= scrapy.Field()
        comments_good= scrapy.Field()
        comments_bad= scrapy.Field()
        desc= scrapy.Field()
        salesdesc1 = scrapy.Field()
        produceyear = scrapy.Field()
        makeyear = scrapy.Field()
        emission = scrapy.Field()
        bodystyle = scrapy.Field()
        frontwheel_backwheel = scrapy.Field()
        wheel = scrapy.Field()
        weight = scrapy.Field()
        fuelvolumn = scrapy.Field()
        baggage = scrapy.Field()
        doors = scrapy.Field()
        approach_angle = scrapy.Field()
        lengthwh = scrapy.Field()
        frontgauge_backgauge_length = scrapy.Field()
        drag_coef = scrapy.Field()
        maxload = scrapy.Field()
        maxbaggage = scrapy.Field()
        passengers = scrapy.Field()
        departure_angle = scrapy.Field()
        motortechnique = scrapy.Field()
        motordesc = scrapy.Field()
        motortype = scrapy.Field()
        powerL = scrapy.Field()
        compress = scrapy.Field()
        cylinder_travel = scrapy.Field()
        valve = scrapy.Field()
        maxpower = scrapy.Field()
        fueltype = scrapy.Field()
        cylinder = scrapy.Field()
        lwv = scrapy.Field()
        method = scrapy.Field()
        motorfactoryname = scrapy.Field()
        petrol = scrapy.Field()
        cylinder_diameter = scrapy.Field()
        cylinder_head_material = scrapy.Field()
        cylinder_body_material = scrapy.Field()
        maxnm = scrapy.Field()
        fuelmethod = scrapy.Field()
        lwvnumber = scrapy.Field()
        motor_position = scrapy.Field()
        cooling_system = scrapy.Field()
        gear = scrapy.Field()
        driveway = scrapy.Field()
        fronthang = scrapy.Field()
        frontbrake = scrapy.Field()
        geardesc = scrapy.Field()
        frontwheel = scrapy.Field()
        sparewheel = scrapy.Field()
        fronthubtype = scrapy.Field()
        drive_width = scrapy.Field()
        drive_load = scrapy.Field()
        drive_wheel = scrapy.Field()
        transmission_way = scrapy.Field()
        assistanttype = scrapy.Field()
        backhang = scrapy.Field()
        backbrake = scrapy.Field()
        platform = scrapy.Field()
        backwheel = scrapy.Field()
        sparehubtype = scrapy.Field()
        backhubtype = scrapy.Field()
        drive_flat = scrapy.Field()
        drive_speed = scrapy.Field()
        maxspeed = scrapy.Field()
        max_grade_angel = scrapy.Field()
        warranty = scrapy.Field()
        accelerate = scrapy.Field()
        airbag = scrapy.Field()
        brakelength = scrapy.Field()
        jsonsave = scrapy.Field()
        infors = scrapy.Field()


class AutohomeItem_network(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    brandname = scrapy.Field()
    brandid = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    Key= scrapy.Field()
    prov_ID= scrapy.Field()
    prov_Name= scrapy.Field()
    prov_Pinyin= scrapy.Field()
    prov_Count= scrapy.Field()
    city_ID= scrapy.Field()
    city_Name= scrapy.Field()
    city_Pinyin= scrapy.Field()
    city_Count= scrapy.Field()
    ####key info
    shopname= scrapy.Field()
    shoptype= scrapy.Field()
    shopcolor= scrapy.Field()
    shopstar= scrapy.Field()
    ####salemodel and saleprice
    modelnumber= scrapy.Field()
    mainbrands= scrapy.Field()
    tel= scrapy.Field()
    saleregion=scrapy.Field()
    priceurl= scrapy.Field()
    ####location
    location= scrapy.Field()
    locationurl= scrapy.Field()
    ####promotion
    promotion= scrapy.Field()
    promotionurl= scrapy.Field()
    ####img
    imageurl= scrapy.Field()

class yicheItem_network(scrapy.Item):
    # define the fields for your item here like:
    # com
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    #bf
    brandname = scrapy.Field()
    brandid = scrapy.Field()
    brandurl = scrapy.Field()
    brandnum = scrapy.Field()
    factoryname = scrapy.Field()
    factoryurl = scrapy.Field()
    factorynum = scrapy.Field()
    #city region
    cityId = scrapy.Field()
    regionId = scrapy.Field()
    cityName = scrapy.Field()
    regionName = scrapy.Field()
    cityPinYin = scrapy.Field()
    parentId = scrapy.Field()
    shortName = scrapy.Field()
    cityLevel = scrapy.Field()
    navCityId = scrapy.Field()
    centerCityId = scrapy.Field()
    type = scrapy.Field()
    ####key info
    shopid= scrapy.Field()
    shopname= scrapy.Field()
    shopfullname = scrapy.Field()
    shoptype= scrapy.Field()
    ####salemodel and saleprice
    mainbrands= scrapy.Field()
    tel= scrapy.Field()
    saleregion=scrapy.Field()
    ####location
    location= scrapy.Field()
    locationurl= scrapy.Field()
    ####promotion
    promotion= scrapy.Field()
    promotionurl= scrapy.Field()
class yicheItem_price(scrapy.Item):
    # define the fields for your item here like:
    # com
    url = scrapy.Field()
    website = scrapy.Field()
    grabtime = scrapy.Field()
    status = scrapy.Field()
    #bf
    brandname = scrapy.Field()
    brandid = scrapy.Field()
    brandurl = scrapy.Field()
    brandnum = scrapy.Field()
    factoryname = scrapy.Field()
    factoryid = scrapy.Field()
    factorynum = scrapy.Field()
    factoryurl = scrapy.Field()
    familyname = scrapy.Field()
    familyid = scrapy.Field()
    familynum = scrapy.Field()
    familyurl = scrapy.Field()
    #model
    modelid= scrapy.Field()
    model= scrapy.Field()
    #city region
    # cityId = scrapy.Field()
    # regionId = scrapy.Field()
    # cityName = scrapy.Field()
    # regionName = scrapy.Field()
    # cityPinYin = scrapy.Field()
    # parentId = scrapy.Field()
    # shortName = scrapy.Field()
    # cityLevel = scrapy.Field()
    # navCityId = scrapy.Field()
    # centerCityId = scrapy.Field()
    type = scrapy.Field()
    ####key info
    shopid= scrapy.Field()
    shopname= scrapy.Field()
    shopfullname = scrapy.Field()
    shoptype= scrapy.Field()
    ####salemodel and saleprice
    mainbrands= scrapy.Field()
    tel= scrapy.Field()
    tel400 = scrapy.Field()
    saleregion=scrapy.Field()
    ####location
    location= scrapy.Field()
    locationurl= scrapy.Field()
    ####promotion
    promotion= scrapy.Field()
    promotionurl= scrapy.Field()
    #price
    price= scrapy.Field()
    price_district= scrapy.Field()
    price_city= scrapy.Field()

#sohu
class SohunewcarItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    brandid = scrapy.Field()
    brandname = scrapy.Field()
    familyid = scrapy.Field()
    familyname = scrapy.Field()
    trimid = scrapy.Field()
    trimname = scrapy.Field()
    trimgear = scrapy.Field()
    trimdisp = scrapy.Field()
    trimyear = scrapy.Field()

class SuhuagencyItem(scrapy.Item):
    grabtime=scrapy.Field()
    url=scrapy.Field()
    status=scrapy.Field()
    website=scrapy.Field()
    datasave=scrapy.Field()
    provinceid=scrapy.Field()
    cityid=scrapy.Field()
    cityname=scrapy.Field()
    agencyid=scrapy.Field()
    agencyname=scrapy.Field()
    mainbrand=scrapy.Field()
    telephone=scrapy.Field()
    adress=scrapy.Field()
    shopclass=scrapy.Field()
    brand=scrapy.Field()
    brandseries=scrapy.Field()

class SohusalesfamilyItem(scrapy.Item):
    grabtime = scrapy.Field()
    url = scrapy.Field()
    status= scrapy.Field()
    website = scrapy.Field()
    brand = scrapy.Field()
    brandname = scrapy.Field()
    factoryname = scrapy.Field()
    familyname = scrapy.Field()
    brandid = scrapy.Field()
    factoryid = scrapy.Field()
    familyid= scrapy.Field()
    saledata=scrapy.Field()

class SohusalescorpItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    brandid = scrapy.Field()
    brandname = scrapy.Field()
    corpname = scrapy.Field()
    corpid = scrapy.Field()
    saledata=scrapy.Field()

class SohusaleslevelItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    level=scrapy.Field()
    classname=scrapy.Field()
    saledata = scrapy.Field()

class SohusalespriceItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    price=scrapy.Field()
    pricename=scrapy.Field()
    saledata = scrapy.Field()

class SohusalesbrandItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    brandname=scrapy.Field()
    brandid=scrapy.Field()
    saledata = scrapy.Field()

class Marketsharetranslation(scrapy.Item):
    index=scrapy.Field()
    model=scrapy.Field()
    results=scrapy.Field()

class ChedaoshanqianItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    cityid=scrapy.Field()
    cityname=scrapy.Field()
    brandid = scrapy.Field()
    brandname = scrapy.Field()
    itemid=scrapy.Field()
    agencyid=scrapy.Field()
    agencyname=scrapy.Field()
    province=scrapy.Field()
    seriesid = scrapy.Field()
    seriesname = scrapy.Field()
    makeyear = scrapy.Field()
    registerdate = scrapy.Field()
    mileage = scrapy.Field()
    price1 = scrapy.Field()
    guideprice = scrapy.Field()
    guidepricetax = scrapy.Field()
    changetimes = scrapy.Field()
    yearchecktime = scrapy.Field()
    Insurance1 = scrapy.Field()
    Insurance2 = scrapy.Field()
    img_url = scrapy.Field()
    agencycarnum = scrapy.Field()
    agencyrate = scrapy.Field()
    agencyattionnum = scrapy.Field()
    agencycity= scrapy.Field()
    agencyphone = scrapy.Field()
    emission = scrapy.Field()
    carsource = scrapy.Field()
    geartype = scrapy.Field()
    output = scrapy.Field()
    color = scrapy.Field()
    body = scrapy.Field()
    shortdesc = scrapy.Field()
    dealtype = scrapy.Field()
    telphone = scrapy.Field()
    desc = scrapy.Field()

class Ic5uItem(scrapy.Item):
    grabtime=scrapy.Field()
    website = scrapy.Field()
    status=scrapy.Field()
    url = scrapy.Field()
    city=scrapy.Field()
    title=scrapy.Field()
    price1=scrapy.Field()
    guideprice = scrapy.Field()
    attention= scrapy.Field()
    registerdate=scrapy.Field()
    mileage=scrapy.Field()
    geartype=scrapy.Field()
    emission=scrapy.Field()
    dealtype= scrapy.Field()
    dealplace = scrapy.Field()
    telephone = scrapy.Field()
    yearchecktime = scrapy.Field()
    Insurance1 = scrapy.Field()
    output= scrapy.Field()
    color = scrapy.Field()
    rate= scrapy.Field()
    ratelist1 = scrapy.Field()
    ratelist2= scrapy.Field()
    ratelist3= scrapy.Field()
    ratelist4= scrapy.Field()
    ratelist5= scrapy.Field()
    checkdesc=scrapy.Field()
    desc= scrapy.Field()
    img = scrapy.Field()

class Indexyichenationm(scrapy.Item):
    grabtime= scrapy.Field()
    website = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()
    dataseason= scrapy.Field()
    region=scrapy.Field()
    level=scrapy.Field()
    datayear=scrapy.Field()
    datamonth= scrapy.Field()
    # dataseason = scrapy.Field()
    data = scrapy.Field()

class SGMfamilymap(scrapy.Item):
    index=scrapy.Field()
    model=scrapy.Field()
    results=scrapy.Field()


