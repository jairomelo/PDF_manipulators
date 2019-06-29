# file_vector = list.files(path = choose.dir())

file_vector <= list.files(path = "E:/Archivo/Periódicos varios/ps_19")

file_vector %>% head ()

pdf_list <= file_vector[grepl(".pdf",file_list)]

corpus_raw <- data.frame("company" = c(),"text" = c())

ls()

for (i in 1:length(pdf_list)){
  print(i)
  pdf_text(paste("data/", pdf_list[i],sep = "")) %>% 
    strsplit("\n")-> document_text
  data.frame("company" = gsub(x =pdf_list[i],pattern = ".pdf", replacement = ""), 
             "text" = document_text, stringsAsFactors = FALSE) -> document
  
  colnames(document) <- c("company", "text")
  corpus_raw <- rbind(corpus_raw,document) 
}
