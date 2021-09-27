import dexml
from dexml import fields

"""
Helper Classes for VAST 2.0
"""

# Fix problem with this class. dexml can't recognize him.
class Click(dexml.Model):
    id = fields.String(attrname="id", required=False)
    uri = fields.CDATA(tagname=".")

class Tracking(dexml.Model):
    event = fields.String(attrname="event")
    trackingUrl = fields.CDATA(tagname=".")

class AdParameters(dexml.Model):
    xmlEncoded = fields.Boolean(attrname="xmlEncoded", required=False)
    data = fields.CDATA(tagname=".")

class IconResource(dexml.Model):
    creativeType = fields.String(required = False)
    data = fields.CDATA(tagname=".")

class AdSystem(dexml.Model):
    version = fields.String(attrname="version", required=False)
    data = fields.String(tagname=".")


"""
Linear Model
VAST 2.0
"""
class Linear(dexml.Model):
    class meta:
        order_sensitive = False
    
    skipoffset = fields.String(required=False)

    adParameters = fields.Model(AdParameters, tagname="AdParameters", required=False)
    duration = fields.String(tagname="Duration")


    """
    MediaFile Model
    VAST 2.0
    """
    class MediaFile(dexml.Model):
        class meta:
            order_sensitive = False
        
        id = fields.String(required=False)
        delivery = fields.String()
        type = fields.String()

        bitrate = fields.String(required=False)
        minBitrate = fields.String(required=False)
        maxBitrate = fields.String(required=False)

        width = fields.String()
        height = fields.String()
        scalable = fields.Boolean(required=False)
        maintainAspectRatio = fields.Boolean(required=False)

        codec = fields.String(required=False)
        apiFramework = fields.String(required=False)

        mediaFileUrl = fields.CDATA(tagname=".")
    
    mediaFiles = fields.List(MediaFile, tagname="MediaFiles")
    trackingEvents = fields.List(Tracking, tagname="TrackingEvents")


    """
    VideoClicks Model
    VAST 2.0
    """
    class VideoClicks(dexml.Model):
        class meta:
            order_sensitive = False
        
        clickThrough = fields.CDATA(tagname="ClickThrough", required=False)
        clickTracking = fields.CDATA(tagname="ClickTracking", required=False)
        customClick = fields.CDATA(tagname="CustomClick", required=False)

    videoClicks = fields.Model(VideoClicks, tagname="VideoClicks", required=False)


    """
    Icon Model
    VAST 2.0
    """
    class Icon(dexml.Model):
        class meta:
            order_sensitive = False
        

        program = fields.String()
        height = fields.String()
        width = fields.String()
        xPosition = fields.String()
        yPosition = fields.String()

        apiFramework = fields.String(required=False)
        offset = fields.String(required=False)
        duration = fields.String(required=False)

        staticResource = fields.Model(IconResource, tagname="StaticResource", required=False)
        iFramResource = fields.Model(IconResource, tagname="IFrameResource", required=False)
        htmlResource = fields.Model(IconResource, tagname="HTMLResource", required=False)

        """
        IconClicks Model
        VAST 2.0
        """
        class IconClicks(dexml.Model):
            # Elements
            iconClickThrough = fields.CDATA(tagname="IconClickThrough", required=False)
            iconClickTracking = fields.CDATA(tagname="IconClickTracking", required=False)
            
        iconClicks = fields.Model(IconClicks, tagname="IconClicks", required=False)
        iconViewTracking = fields.CDATA(tagname="IconViewTracking", required=False)
    
    icons = fields.List(Icon, tagname="Icons", required=False)


"""
CompanionAds Model
VAST 2.0
"""
class CompanionAds(dexml.Model):
    class meta:
        order_sensitive = False
    
    required = fields.String(required=False)

    """
    Companion Model
    VAST 2.0
    """

    class Companion(dexml.Model):
        class meta:
            order_sensitive = False
        
        width = fields.String()
        height = fields.String()

        id = fields.String(required=False)
        assetWidth = fields.String(required=False)
        assetHeight = fields.String(required=False)
        expandedWidth = fields.String(required=False)
        expandedHeight = fields.String(required=False)
        apiFramework = fields.String(required=False)
        adSlotID = fields.String(required=False)
        required = fields.String(required=False)

        staticResource = fields.Model(IconResource, tagname="StaticResource", required=False)
        iFramResource = fields.Model(IconResource, tagname="IFrameResource", required=False)
        htmlResource = fields.Model(IconResource, tagname="HTMLResource", required=False)
        
        adParameters = fields.Model(AdParameters, tagname="AdParameters", required=False)
        altText = fields.String(tagname="AltText", required=False)

        companionClickThrough = fields.CDATA(tagname="CompanionClickThrough", required=False)
        companionClickTracking = fields.CDATA(tagname="CompanionClickTracking", required=False)
        trackingEvents = fields.List(Tracking, tagname="TrackingEvents", required=False)


    companions = fields.List(fields.Model(Companion, tagname="Companion"))


"""
NonLinearAds Model
VAST 2.0
"""
class NonLinearAds(dexml.Model):
    class meta:
        order_sensitive = False
    

    """
    NonLinear Model
    VAST 2.0
    """
    class NonLinear(dexml.Model):
        class meta:
            order_sensitive = False
        
        width = fields.String()
        height = fields.String()

        id = fields.String(required=False)
        expandedWidth = fields.String(required=False)
        expandedHeight = fields.String(required=False)
        scalable = fields.Boolean(required=False)
        maintainAspectRatio = fields.Boolean(required=False)
        minSuggestedDuration = fields.String(required=False)
        apiFramework = fields.String(required=False)

        staticResource = fields.Model(IconResource, tagname="StaticResource", required=False)
        iFramResource = fields.Model(IconResource, tagname="IFrameResource", required=False)
        htmlResource = fields.Model(IconResource, tagname="HTMLResource", required=False)

        nonLinearClickThrough = fields.CDATA(tagname="NonLinearClickThrough", required=False)
        nonLinearClickTracking = fields.CDATA(tagname="NonLinearClickTracking", required=False)

        adParameters = fields.Model(AdParameters, tagname="AdParameters", required=False)
    

    nonLinears = fields.List(NonLinear)
    trackingEvents = fields.List(Tracking, tagname="TrackingEvents", required=False)

"""
Creative Model
VAST 2.0
"""
class Creative(dexml.Model):
    class meta:
        order_sensitive = False
    
    id = fields.String(required=False)
    sequence = fields.String(required=False)
    apiFramework = fields.String(required=False)

    linear = fields.Model(Linear, required=False)
    companionAds = fields.Model(CompanionAds, required=False)

"""
InLine Model
VAST 2.0
"""
class InLine(dexml.Model):
    class meta:
        order_sensitive = False
    
    adSystem = fields.Model(AdSystem, tagname="AdSystem")
    adTitle = fields.String(tagname="AdTitle")

    description = fields.String(tagname="Description", required=False)
    advertiser = fields.String(tagname="Advertiser", required=False)
    surveyUri = fields.CDATA(tagname="Survey", required=False)
    errorUri = fields.CDATA(tagname="Error", required=False)

    """
    Pricing Model
    VAST 2.0
    """
    class Pricing(dexml.Model):
        class meta:
            order_sensitive = False
        
        model = fields.String()
        currency = fields.String()

        data = fields.CDATA(tagname=".")

    pricing = fields.Model(Pricing, required=False)

    class Impression(dexml.Model):
        impressionUri = fields.CDATA(tagname=".")
    
    impressions = fields.List(Impression)
    creatives = fields.List(Creative, tagname="Creatives")


"""
Wrapper Model
VAST 2.0
"""
class Wrapper(dexml.Model):
    class meta:
        order_sensitive = False
    
    adSystem = fields.Model(AdSystem, tagname="AdSystem")
    vastAdTagURI = fields.CDATA(tagname="VASTAdTagURI")

    errorUri = fields.CDATA(tagname="Error", required=False)
    impression = fields.CDATA(tagname="Impression")
    creatives = fields.List(Creative, tagname="Creatives", required=False)

"""
Ad Model
VAST 2.0
"""
class Ad(dexml.Model):
    class meta:
        order_sensitive = False
    
    id = fields.String(required=False)
    sequence = fields.String(required=False)

    inLine = fields.Model(InLine, required=False)
    wrapper = fields.Model(Wrapper, required=False)

"""
VAST Model
VAST 2.0
"""
class VAST(dexml.Model):
    class meta:
        order_sensitive = False
    
    version = fields.String()
    errorData = fields.CDATA(tagname="Error", required=False)

    ad = fields.Model(Ad, tagname="Ad")