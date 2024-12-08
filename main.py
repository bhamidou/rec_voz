import argparse
import asyncio
from services.voice_assistant import start_voice_assistant


if __name__ == "__main__":
    print('''
⠀⠀
  .oooooo.   oooo   o8o                                                            o8o            
 d8P'  `Y8b  `888   `"'                                                            `"'            
888           888  oooo  ooo. .oo.  .oo.    .oooo.                     oo.ooooo.  oooo   .oooo.   
888           888  `888  `888P"Y88bP"Y88b  `P  )88b                     888' `88b `888  `P  )88b  
888           888   888   888   888   888   .oP"888       8888888       888   888  888   .oP"888  
`88b    ooo   888   888   888   888   888  d8(  888                     888   888  888  d8(  888  
 `Y8bood8P'  o888o o888o o888o o888o o888o `Y888""8o                    888bod8P' o888o `Y888""8o 
                                                                        888                       
                                                                       o888o                      
                                                                                                 
          ''')
    
    start_voice_assistant()

