for i in $(seq 1 149); do
curl $"https://www.moonboard.com/Content/images/Holds/h$i.png" -H 'Referer: https://www.moonboard.com/HoldSetups/Index' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' --compressed > "hold_pngs/$i".png
done

