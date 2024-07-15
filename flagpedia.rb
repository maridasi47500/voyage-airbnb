require "nokogiri"
require "open-uri"
require "json"
@doc=Nokogiri::HTML(URI.open("https://flagpedia.net/index"))
@pays=[]
@doc.css("[data-area]").each do |x|
  begin
    pays={}
    pays["country"]=x.text.strip
    ###############
    @doc2=Nokogiri::HTML(URI.open("https://flagpedia.net"+x.attributes["href"].value+"/emoji"))
    hey=@doc2.css("table td")[1].text.gsub("&amp;","&")
    pays["unicode"]=hey
    ################

    ####################
    @doc3=Nokogiri::HTML(URI.open("https://flagpedia.net"+x.attributes["href"].value+""))
    if @doc3.css("table td").length > 12
      currency=@doc3.css("table td")[11].text
      pays["currency"]=currency
      callingcode=@doc3.css("table td")[12].text
      pays["callingcode"]=callingcode
      countrycode=@doc3.css("table td")[13].text.gsub(".","").split(",")[0]
      pays["countrycode"]=countrycode
      #p ("https://dayspedia.com/time/"+countrycode+"")
      @doc4=Nokogiri::HTML(URI.open("https://dayspedia.com/time/"+countrycode+"/"))
      #p @doc4.css("a[href*='/time/zones/utc']")
      timezone=@doc4.css("a[href*='/time/zones/utc']")[0].text.gsub("UTC","")
      pays["timezone"]=timezone
      
    end
    ############


    p pays
    @pays<<pays
    File.write("public/flag.json", JSON.pretty_generate({"pays":@pays}))
  rescue => e
    @pays<<pays
    p pays
    File.write("public/flag.json", JSON.pretty_generate({"pays":@pays}))
    #p e
    next
  end
end

