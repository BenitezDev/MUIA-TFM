import os
import fujiwrapper

if __name__ == '__main__':
	fuji = fujiwrapper.FujiWrapper()
	fuji_results = fuji.get_metric("https://doi.org/10.1186/2041-1480-4-37")
	print(fuji_results)




