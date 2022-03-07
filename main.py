import fujiwrapper
import foopswrapper

if __name__ == '__main__':

	fuji = fujiwrapper.FujiWrapper()
	fuji_results = fuji.get_metric("https://doi.org/10.1186/2041-1480-4-37")
	print("F-UJI results:", fuji_results)


	foops = foopswrapper.FoopsWrapper(8888)
	foops_results = foops.get_metric("https://w3id.org/okn/o/sd")
	print("Foops results:", foops_results)




