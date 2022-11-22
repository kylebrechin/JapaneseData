using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

struct SentenceType {
            public bool has_furigana;
            public string sentence_data;
}

public class TextParser : MonoBehaviour
{
    
        public void ParseText()
        {
            
            
            string first_sentence = "[犬:いぬ]の[散歩:さんぽ]は[私:わたし]の[日課:にっか]です。";
            string second_sentence = "「ゆっくり[歩:ある]く」の「ゆっくり」は[副詞:ふくし]です。";
            string third_sentence = "[上野:うえの][駅:えき]は[面白い:おもしろい]ですね。";
            string fourth_sentence = "[上野:うえの]は[面白い:おもしろい]";
            string fifth_sentence = "こんにちは！";
            
            // create a list of lines to store all the information
            List<SentenceType> lines = new List<SentenceType>();

            string sentence = second_sentence;
            
            if(sentence.Contains('[')){
                // see how many times we'll have to process the loop
                int bracket_count = 0;
                foreach (char c in sentence)
                    if(c == '[') bracket_count++;
                
                //while(bracket_count > 0) {
                //while(sentence.Contains('['))    {
                while(!string.IsNullOrEmpty(sentence))    {    
                    //Console.ReadLine();
                    // get all indices for BRACKETS [
                    int bracket_index = sentence.IndexOf('[');

                    if(bracket_index == 0) {
                        // find closing bracket
                        int matching_index = sentence.IndexOf(']');
                        string caught_characters = "";
                        // put everything between [ ] into a variable
                        try {
                            caught_characters = sentence.Remove(matching_index+1);
                        }
                        catch (ArgumentOutOfRangeException e) {
                            
                            caught_characters = sentence;
                            
                            if(caught_characters.Contains('[')) {
                                SentenceType data = new SentenceType{ has_furigana = true, sentence_data = caught_characters };
                                lines.Add(data);
                            }
                            else {
                                SentenceType data = new SentenceType{ has_furigana = false, sentence_data = caught_characters };
                                lines.Add(data);
                            }
                            break;
                        }
                        sentence = sentence.Substring(matching_index+1);
                        // update the sentence with whatever is left to process

                        if(caught_characters.Contains('[')) {
                            SentenceType data = new SentenceType{ has_furigana = true, sentence_data = caught_characters };
                            lines.Add(data);
                        }
                        else {
                            SentenceType data = new SentenceType{ has_furigana = false, sentence_data = caught_characters };
                            lines.Add(data);
                        }
                    } else if (bracket_index > 0) {    // BRACKET IS NOT FIRST
                        //Console.WriteLine("Found a bracket elsewhere. {0}", bracket_index);
                        string caught_characters = sentence.Remove(bracket_index);
                        sentence = sentence.Substring(bracket_index);
                        

                        if(caught_characters.Contains('[')) {
                            SentenceType data = new SentenceType{ has_furigana = true, sentence_data = caught_characters };
                            lines.Add(data);
                        }
                        else {
                            SentenceType data = new SentenceType{ has_furigana = false, sentence_data = caught_characters };
                            lines.Add(data);
                        }                        
                    } else if (bracket_index < 0) {
                        // SEND TO LIST                        
                        if(sentence.Contains('[')) {
                            SentenceType data = new SentenceType{ has_furigana = true, sentence_data = sentence };
                            lines.Add(data);
                        }
                        else {
                            SentenceType data = new SentenceType{ has_furigana = false, sentence_data = sentence };
                            lines.Add(data);
                        }
                        sentence = "";
                    }
                    bracket_count--;
                }
            }
            else {
                if(sentence.Contains('[')) {
                    SentenceType data = new SentenceType{ has_furigana = true, sentence_data = sentence };
                    lines.Add(data);
                }
                else {
                    SentenceType data = new SentenceType{ has_furigana = false, sentence_data = sentence };
                    lines.Add(data);
                }
            }

            for(int i = 0; i < lines.Count; i++) {
                Console.WriteLine(lines[i].has_furigana + ", " + lines[i].sentence_data);
            }
        } // END MAIN
}
