# Found in Google & Sotify
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # Input:

        # n : number of songs available
        # goal : size of playlist
        # k : no of unique songs that must be played in series before that same song can be repeated
        mod = 10**9 +7


        cache = {}
        def recur(playlist_len, num_old_songs):

            # Trying to create playlist:
            # playlist = []
            # Stopping conditions

            # num_old_songs : this value will be the iterating value from 1 to n
                

            # 1) reached reqd playlist size: 
            # if playlist_len ==0:
                # if num_old_songs == n: 
                    # WE have chosen all available songs atleast once
                    # i.e playlist populated with songs ranging from 1 to n
                    
            if playlist_len == 0 and num_old_songs == n:
                # old_song = num_old_songs
                # playlist.append(old_song)
                return 1  # 1 playlist generated , This value will need to be added


            # Note: This case is going to happen when the recursive calls go out of bounds to choose a VOID song (value beyond n)
            # 2) We filled a playlist but reached a point where a invalid object was considered for a song (value beyond n)

            if playlist_len == 0 or num_old_songs > n:
                return 0 # Invalid playlist
            
            # return cached
            if (playlist_len, num_old_songs) in cache:
                return cache[(playlist_len, num_old_songs)]
            # Now we choose songs:

            # If we choose a NEW song to the playlist: 
            # 1> playlist_len decreases by 1
            # 2> num_old_songs increases by 1
            # This is where we could possibly choose a VOID song!  (num_old_songs > n)
            # At stopping point , recur(playlist_len-1,num_old_songs+1) will generate 0 or 1
            # How do we generate our count?

            playlist_count = recur(playlist_len-1,num_old_songs+1)

            available_newsongs = (n-num_old_songs)
            # The math:

            num_playlists = available_newsongs * playlist_count  

            # we might also have to choose an old song, this is when they have provided n<goal
            # We check if num_old_songs > k : This indicates the concept of gap
            # Eg when k = 2 , and playlist looks like [1,2,3] , since num_old_songs = 3 , we can repeat 1 num since 
            #  num_old_songs > k
            if num_old_songs > k:

                # playlist_count = recur(playlist_len-1, num_old_songs)
                # The math:
                num_playlists += (num_old_songs-k) * recur(playlist_len-1, num_old_songs)

            # caches results
            cache[(playlist_len, num_old_songs)] = num_playlists % mod
            return  cache[(playlist_len, num_old_songs)]
            
        res = recur(goal , 0)
        return res