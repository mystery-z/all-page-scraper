require 'httparty'
require 'net/http'

#works to some extent

a = 3
#getting words from the dictionary - special thanks to https://github.com/dwyl/english-words
word_list = IO.readlines("words.txt", chomp: true)

puts "How many sites would you like to parse through? type 370103 for all"
count = gets.chomp
count = count.to_i
count = count +3

time = Time.new

now = time.strftime("%Y-%m-%d")
now = now.to_s
file_name = "output-#{now}"
out_file = File.new("#{file_name}.txt", "w")
output_txt = ""

while a < count
	#sorts words
	res_body = ""
	word_list = IO.readlines("words.txt", chomp: true)
	word_spec_num = word_list[a]
	puts "\n\n" 
	output_txt = "#{output_txt} \n"
	puts word_spec_num
	output_txt = "#{output_txt}#{word_spec_num}"
	uri = URI "https://#{word_spec_num}.com/"
	puts "link: #{uri}"
	output_txt = "#{output_txt} \n #{uri}"
	#end of word x URL-ing
	begin
		params = { :limit => 200, :page => 3 }
		uri.query = URI.encode_www_form(params)
		res = Net::HTTP.get_response(uri)
		res_body = res.body if res.is_a?(Net::HTTPSuccess)
		puts res_body
		output_txt = "#{output_txt} \n #{res_body}"
	rescue
		puts "error"
		output_txt = "#{output_txt}, \n error \n"
	#error code 200 means its ok to proceed
	end	
	a = a+1
end

puts "end"
f = File.open("output-#{now}.txt", 'w')  
f.write(output_txt)
f.close
