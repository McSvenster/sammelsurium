#!/usr/bin/env ruby

class Record
  attr_reader :lines
  def initialize(sysno)
    @sysno = sysno
    @lines = []
  end

  def add_line(line)
    @lines << line
  end

  def write(of)
    outputfile = File.open(of,"a")
    self.lines.each do |line|
      outputfile.puts line
    end
    outputfile.close
  end

  def really_keep?
    ohne_6xx = true
    ohne_isbn = true
    e65exemplar = false
    self.lines.each do |line|
      if line[10] == "6"
        ohne_6xx = false
      end
      if line[10..12] == "020"
        ohne_isbn = false
      end
      if line =~ /^\d{9} 940 .*\$\$fE65/
        e65exemplar = true
      end
    end
    return ohne_6xx && ohne_isbn && e65exemplar
  end

end

dateiname = ARGV[0]
feld = ARGV[1]
qstring = ARGV[2].chomp
of = "e65-records_with_#{feld}_with_#{qstring}_without-isbn.sequa"
sysno_file = File.open("e65-sysnos_#{feld}_#{qstring}_without-isbn.txt", "w")

(5 - feld.size).times do
  feld += " "
end

sysno = ""
keep_record = false
File.foreach(dateiname, :encoding => 'ISO-8859-1').with_index do |line, line_num|
  if line[0..8] != sysno
    if keep_record
      if @record.really_keep?
        puts "writing Record #{sysno} with #{@record.lines.size} lines"
        @record.write(of)
        sysno_file.puts sysno
      end
    end
    sysno = line[0..8]
    @record = Record.new(sysno)
    keep_record = false
  end

  @record.add_line(line)
  if line =~ /^\d{9} #{feld} .*#{qstring}/
    keep_record = true
  end

  
end

sysno_file.close